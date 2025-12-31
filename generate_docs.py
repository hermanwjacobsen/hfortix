#!/usr/bin/env python3
"""
Generate Sphinx RST documentation from FortiOS API Python modules.

This script introspects the actual Python code in packages/fortios/hfortix_fortios/api/v2/
and generates accurate RST documentation with correct:
- Method signatures with explicit parameters
- Example code showing actual usage
- Proper hierarchy matching the API structure
"""

import ast
import inspect
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


class MethodInfo:
    """Information about a method extracted from code."""
    
    def __init__(self, name: str, params: List[Tuple[str, str, Any]], docstring: Optional[str]):
        self.name = name
        self.params = params  # List of (name, type_hint, default)
        self.docstring = docstring or ""


class EndpointInfo:
    """Information about an API endpoint."""
    
    def __init__(self, category: str, path: str, class_name: str):
        self.category = category  # e.g., 'cmdb', 'monitor', 'log', 'service'
        self.path = path  # e.g., 'alertemail/setting', 'firewall/address'
        self.class_name = class_name
        self.methods: Dict[str, MethodInfo] = {}
        self.module_docstring = ""


def parse_function_signature(func_node: ast.FunctionDef) -> List[Tuple[str, str, Any]]:
    """Parse function signature to extract parameters with types and defaults."""
    params = []
    
    for arg in func_node.args.args:
        if arg.arg == 'self':
            continue
            
        # Get type annotation
        type_hint = ""
        if arg.annotation:
            type_hint = ast.unparse(arg.annotation)
        
        # Get default value
        default = None
        num_defaults = len(func_node.args.defaults)
        num_args = len(func_node.args.args) - 1  # Exclude self
        arg_index = func_node.args.args.index(arg) - 1  # Exclude self
        
        if arg_index >= (num_args - num_defaults):
            default_index = arg_index - (num_args - num_defaults)
            default_node = func_node.args.defaults[default_index]
            default = ast.unparse(default_node)
        
        params.append((arg.arg, type_hint, default))
    
    # Handle **kwargs
    if func_node.args.kwarg:
        params.append((f"**{func_node.args.kwarg.arg}", "Any", None))
    
    return params


def extract_docstring(node: ast.AST) -> Optional[str]:
    """Extract docstring from AST node."""
    if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
        if (node.body and 
            isinstance(node.body[0], ast.Expr) and 
            isinstance(node.body[0].value, ast.Constant) and
            isinstance(node.body[0].value.value, str)):
            return node.body[0].value.value
    return None


def parse_endpoint_file(file_path: Path, category: str) -> Optional[EndpointInfo]:
    """Parse a single endpoint Python file."""
    with open(file_path, 'r') as f:
        content = f.read()
    
    try:
        tree = ast.parse(content)
    except SyntaxError:
        print(f"Failed to parse {file_path}")
        return None
    
    module_docstring = extract_docstring(tree)
    
    # Find the main class
    main_class = None
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Skip nested classes and private classes
            if not node.name.startswith('_'):
                main_class = node
                break
    
    if not main_class:
        return None
    
    # Extract path from file structure
    # e.g., .../v2/cmdb/alertemail/setting.py -> alertemail/setting
    parts = file_path.parts
    v2_index = parts.index('v2')
    category_index = v2_index + 1
    path_parts = parts[category_index + 1:]  # Skip category (cmdb, monitor, etc)
    
    # Remove .py extension from last part
    path_parts = list(path_parts)
    path_parts[-1] = path_parts[-1].replace('.py', '')
    
    endpoint_path = '/'.join(path_parts)
    
    endpoint = EndpointInfo(category, endpoint_path, main_class.name)
    endpoint.module_docstring = module_docstring or ""
    
    # Extract methods (get, post, put, delete)
    for item in main_class.body:
        if isinstance(item, ast.FunctionDef):
            if item.name in ('get', 'post', 'put', 'delete'):
                params = parse_function_signature(item)
                docstring = extract_docstring(item)
                endpoint.methods[item.name] = MethodInfo(item.name, params, docstring)
    
    return endpoint


def generate_method_example(endpoint: EndpointInfo, method_name: str, method: MethodInfo) -> str:
    """Generate example code for a method."""
    examples = []
    
    # Build the access path
    path_parts = endpoint.path.replace('/', '.').replace('-', '_')
    access_path = f"fgt.api.{endpoint.category}.{path_parts}.{method_name}"
    
    if method_name == 'get':
        # List all
        examples.append(f"   # List all items")
        examples.append(f"   items = {access_path}()")
        examples.append("")
        
        # Get specific (if name parameter exists)
        if any(p[0] == 'name' for p in method.params):
            examples.append(f"   # Get specific item by name")
            examples.append(f"   item = {access_path}(name='item-name')")
        
    elif method_name == 'post':
        examples.append(f"   # Create new item")
        
        # Find required parameters (those without defaults, excluding special ones)
        required = [p for p in method.params 
                   if p[2] is None and p[0] not in ('payload_dict', 'vdom', 'raw_json') 
                   and not p[0].startswith('**')]
        
        # Find common optional parameters
        optional = [p for p in method.params[:15]  # First 15 to keep it reasonable
                   if p[2] is not None and p[0] not in ('payload_dict', 'before', 'after', 'vdom', 'raw_json')
                   and not p[0].startswith('**')]
        
        call_parts = [f"   result = {access_path}("]
        
        if required:
            for param_name, _, _ in required[:3]:  # Show first 3 required
                call_parts.append(f"       {param_name}='value',")
        
        if optional:
            for param_name, _, _ in optional[:3]:  # Show first 3 optional
                call_parts.append(f"       {param_name}='value',  # optional")
        
        call_parts.append("   )")
        
        examples.extend(call_parts)
        
    elif method_name == 'put':
        examples.append(f"   # Update existing item")
        
        # Find common parameters
        params_to_show = [p for p in method.params[:15]
                         if p[0] not in ('payload_dict', 'before', 'after', 'vdom', 'raw_json')
                         and not p[0].startswith('**')]
        
        call_parts = [f"   result = {access_path}("]
        
        for param_name, _, _ in params_to_show[:4]:  # Show first 4
            call_parts.append(f"       {param_name}='updated-value',")
        
        call_parts.append("   )")
        examples.extend(call_parts)
        
    elif method_name == 'delete':
        examples.append(f"   # Delete item")
        
        # Check if it has name parameter
        if any(p[0] == 'name' for p in method.params):
            examples.append(f"   result = {access_path}(name='item-name')")
        else:
            examples.append(f"   result = {access_path}()")
    
    return '\n'.join(examples)


def generate_rst_file(endpoint: EndpointInfo, output_dir: Path):
    """Generate RST documentation file for an endpoint."""
    
    # Create directory structure
    category_dir = output_dir / endpoint.category / endpoint.path.rsplit('/', 1)[0] if '/' in endpoint.path else output_dir / endpoint.category
    category_dir.mkdir(parents=True, exist_ok=True)
    
    # File name is the last part of the path
    filename = endpoint.path.split('/')[-1] + '.rst'
    output_file = category_dir / filename
    
    # Build access path for Python attribute
    path_for_attr = endpoint.path.replace('/', '.').replace('-', '_')
    python_attr = f"fgt.api.{endpoint.category}.{path_for_attr}"
    
    # Extract title from class name or path
    title = endpoint.class_name
    
    lines = [
        title,
        "=" * len(title),
        "",
        f"Configuration endpoint for {endpoint.path}.",
        "",
        "Python Attribute",
        "----------------",
        "",
        ".. code-block:: python",
        "",
        f"   {python_attr}",
        "",
    ]
    
    # Add available methods section
    if endpoint.methods:
        lines.extend([
            "Available Methods",
            "-----------------",
            "",
        ])
        
        for method_name in ['get', 'post', 'put', 'delete']:
            if method_name in endpoint.methods:
                method = endpoint.methods[method_name]
                lines.append(f"- ``{method_name}()`` - {method_name.upper()} operation")
        
        lines.append("")
    
    # Add examples for each method
    if endpoint.methods:
        lines.extend([
            "Examples",
            "--------",
            "",
            ".. code-block:: python",
            "",
            "   from hfortix_fortios import FortiOS",
            "   ",
            "   fgt = FortiOS(host='192.168.1.99', token='your-token')",
            "",
        ])
        
        for method_name in ['get', 'post', 'put', 'delete']:
            if method_name in endpoint.methods:
                method = endpoint.methods[method_name]
                example = generate_method_example(endpoint, method_name, method)
                if example:
                    lines.append(example)
                    lines.append("")
    
    # Add method reference
    if endpoint.methods:
        lines.extend([
            "",
            "Method Reference",
            "----------------",
            "",
        ])
        
        for method_name in ['get', 'post', 'put', 'delete']:
            if method_name in endpoint.methods:
                method = endpoint.methods[method_name]
                
                lines.append(f"``{method_name}()``")
                lines.append("^" * (len(method_name) + 4))
                lines.append("")
                
                # Add signature
                lines.append(".. code-block:: python")
                lines.append("")
                
                # Build signature
                sig_parts = [f"   {method_name}("]
                for i, (param_name, type_hint, default) in enumerate(method.params[:15]):  # Limit to keep readable
                    if param_name.startswith('**'):
                        sig_parts.append(f"       {param_name}")
                    elif default is not None:
                        sig_parts.append(f"       {param_name}={default},")
                    else:
                        sig_parts.append(f"       {param_name},")
                
                if len(method.params) > 15:
                    sig_parts.append("       # ... more parameters")
                
                sig_parts.append("   )")
                
                lines.extend(sig_parts)
                lines.append("")
                
                # Add brief description from docstring
                if method.docstring:
                    first_line = method.docstring.strip().split('\n')[0]
                    lines.append(first_line)
                    lines.append("")
                
                lines.append("")
    
    # Write file
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Generated: {output_file}")
    return output_file


def main():
    """Main entry point."""
    # Base paths
    base_dir = Path(__file__).parent
    api_dir = base_dir / 'packages' / 'fortios' / 'hfortix_fortios' / 'api' / 'v2'
    output_dir = base_dir / 'docs' / 'source' / 'fortios' / 'api-reference'
    
    if not api_dir.exists():
        print(f"API directory not found: {api_dir}")
        return
    
    print(f"Scanning API directory: {api_dir}")
    print(f"Output directory: {output_dir}")
    print()
    
    # Scan all categories
    categories = ['cmdb', 'monitor', 'log', 'service']
    
    endpoints_processed = 0
    
    for category in categories:
        category_dir = api_dir / category
        if not category_dir.exists():
            continue
        
        print(f"\nProcessing category: {category}")
        print("-" * 40)
        
        # Find all Python files
        for py_file in category_dir.rglob('*.py'):
            if py_file.name == '__init__.py':
                continue
            
            endpoint = parse_endpoint_file(py_file, category)
            if endpoint and endpoint.methods:
                generate_rst_file(endpoint, output_dir)
                endpoints_processed += 1
    
    print()
    print("=" * 40)
    print(f"Processed {endpoints_processed} endpoints")
    print("=" * 40)


if __name__ == '__main__':
    main()
