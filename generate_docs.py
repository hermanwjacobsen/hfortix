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


def parse_docstring_params(docstring: str) -> Dict[str, str]:
    """
    Parse parameter descriptions from a Google-style docstring.
    
    Returns:
        Dictionary mapping parameter names to their descriptions
    """
    if not docstring:
        return {}
    
    param_descriptions = {}
    in_args_section = False
    current_param = None
    current_desc_lines = []
    
    for line in docstring.split('\n'):
        stripped = line.strip()
        
        # Check if we're entering the Args section
        if stripped == 'Args:':
            in_args_section = True
            continue
        
        # Check if we're leaving the Args section (another section starts)
        if in_args_section and stripped and not line.startswith(' '):
            break
        
        if in_args_section and stripped.endswith(':') and not stripped.startswith('Args:'):
            # Check if we're entering another section like Returns, Common Query Parameters, etc.
            if stripped in ['Returns:', 'Raises:', 'Examples:', 'Common Query Parameters (via **kwargs):']:
                break
        
        if in_args_section and ':' in stripped:
            # Save previous parameter if exists
            if current_param:
                param_descriptions[current_param] = ' '.join(current_desc_lines).strip()
            
            # Parse new parameter line (format: "param_name: Description")
            parts = stripped.split(':', 1)
            current_param = parts[0].strip()
            current_desc_lines = [parts[1].strip()] if len(parts) > 1 else []
        elif in_args_section and stripped and current_param:
            # Continuation of previous parameter description
            current_desc_lines.append(stripped)
    
    # Save last parameter
    if current_param:
        param_descriptions[current_param] = ' '.join(current_desc_lines).strip()
    
    return param_descriptions


def detect_identifier_field(method: MethodInfo) -> Optional[str]:
    """
    Detect the identifier field used by a method (e.g., 'name', 'policyid', 'id', 'mkey').
    
    Looks for patterns like:
    - raise ValueError("policyid is required for put()")
    - if not name:
    - endpoint = f"/firewall/policy/{policyid}"
    """
    # Check docstring for required parameter mentions
    if method.docstring:
        for line in method.docstring.split('\n'):
            line = line.strip().lower()
            # Look for patterns like "policyid: ... (required)"
            if '(required)' in line:
                for param_name, _, _ in method.params:
                    if param_name.lower() in line and not param_name.startswith('**'):
                        return param_name
    
    # Check common identifier parameter names
    common_identifiers = ['policyid', 'mkey', 'id', 'name']
    for identifier in common_identifiers:
        if any(p[0] == identifier for p in method.params):
            return identifier
    
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
    
    # Detect identifier field (name, policyid, id, mkey, etc.)
    identifier = detect_identifier_field(method)
    
    if method_name == 'get':
        # List all
        examples.append(f"   # List all items")
        examples.append(f"   items = {access_path}()")
        examples.append("")
        
        # Get specific (if identifier parameter exists)
        if identifier:
            examples.append(f"   # Get specific item by {identifier}")
            examples.append(f"   item = {access_path}({identifier}='value')")
        
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
        identifier_label = identifier if identifier else 'identifier'
        examples.append(f"   # Update existing item ({identifier_label} required to identify which item)")
        
        # Find common parameters (exclude special ones)
        params_to_show = [p for p in method.params[:15]
                         if p[0] not in ('payload_dict', 'before', 'after', 'vdom', 'raw_json')
                         and not p[0].startswith('**')]
        
        call_parts = [f"   result = {access_path}("]
        
        # Show identifier first if it exists (it's required for put)
        if identifier:
            call_parts.append(f"       {identifier}='item-identifier',  # Required: identifies which item to update")
        
        # Show other parameters
        other_params = [p for p in params_to_show if p[0] != identifier][:3]
        for param_name, _, _ in other_params:
            call_parts.append(f"       {param_name}='updated-value',")
        
        call_parts.append("   )")
        examples.extend(call_parts)
        
    elif method_name == 'delete':
        examples.append(f"   # Delete item")
        
        # Check if it has identifier parameter (it's required for delete)
        if identifier:
            examples.append(f"   result = {access_path}({identifier}='item-identifier')  # {identifier} required")
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
                lines.append("^" * (len(method_name) + 6))
                lines.append("")
                
                # Add signature
                lines.append(".. code-block:: python")
                lines.append("")
                
                # Build signature - show ALL parameters
                sig_parts = [f"   {method_name}("]
                for i, (param_name, type_hint, default) in enumerate(method.params):
                    if param_name.startswith('**'):
                        sig_parts.append(f"       {param_name}")
                    elif default is not None:
                        sig_parts.append(f"       {param_name}={default},")
                    else:
                        sig_parts.append(f"       {param_name},")
                
                sig_parts.append("   )")
                
                lines.extend(sig_parts)
                lines.append("")
                
                # Add brief description from docstring
                if method.docstring:
                    first_line = method.docstring.strip().split('\n')[0]
                    lines.append(first_line)
                    lines.append("")
                
                # Add important notes for PUT and DELETE
                if method_name in ('put', 'delete'):
                    identifier = detect_identifier_field(method)
                    if identifier:
                        lines.append(".. important::")
                        lines.append(f"   The ``{identifier}`` parameter is **required** for ``{method_name}()`` to identify which item to {method_name}.")
                        lines.append("")
                
                # Add parameter descriptions
                param_descriptions = parse_docstring_params(method.docstring)
                if param_descriptions:
                    lines.append("**Parameters:**")
                    lines.append("")
                    # Detect identifier for marking it as required
                    identifier = detect_identifier_field(method)
                    for param_name, type_hint, default in method.params:
                        if param_name.startswith('**'):
                            # Skip **kwargs for parameter list
                            continue
                        if param_name in param_descriptions:
                            desc = param_descriptions[param_name]
                            # Mark identifier parameter as required for PUT and DELETE
                            if method_name in ('put', 'delete') and param_name == identifier:
                                lines.append(f"- ``{param_name}`` (**required**): {desc}")
                            else:
                                lines.append(f"- ``{param_name}``: {desc}")
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
