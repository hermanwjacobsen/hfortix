#!/usr/bin/env python3
"""
Clean up old manually-created documentation files that have been replaced
by auto-generated ones.

This script identifies and removes old endpoint documentation files that:
1. Use the old format with json= syntax
2. Have hyphens in filenames (old) vs underscores (new)
3. Are not index files or other special files
"""

import os
import re
from pathlib import Path


def is_old_doc_file(filepath: Path) -> bool:
    """Check if a file is an old manually-created doc (vs generated)."""
    
    # Skip index files and special files
    if filepath.name == 'index.rst':
        return False
    
    if filepath.name in ['convenience-wrappers.rst']:
        return False
    
    # Read file content
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except:
        return False
    
    # Check for old patterns
    has_json_syntax = bool(re.search(r"json=\{['\"]", content))
    has_old_mkey = bool(re.search(r"mkey=['\"]item-name['\"]", content) and 
                       not re.search(r"name=['\"]", content))
    
    # Files with hyphens in name are usually old (new ones use underscores)
    has_hyphen_name = '-' in filepath.stem and filepath.stem != 'convenience-wrappers'
    
    # Check for old-style parameter documentation (the giant parameter lists)
    has_old_params = bool(re.search(r'\*\*datasource\*\* \(query\)', content))
    
    return has_json_syntax or (has_hyphen_name and not has_old_params) or has_old_mkey


def find_old_docs(base_dir: Path) -> list[Path]:
    """Find all old documentation files."""
    old_files = []
    
    # Scan all RST files
    for rst_file in base_dir.rglob('*.rst'):
        if is_old_doc_file(rst_file):
            old_files.append(rst_file)
    
    return old_files


def main():
    """Main entry point."""
    base_dir = Path(__file__).parent / 'docs' / 'source' / 'fortios' / 'api-reference'
    
    if not base_dir.exists():
        print(f"Directory not found: {base_dir}")
        return
    
    print("Scanning for old documentation files...")
    print(f"Base directory: {base_dir}")
    print()
    
    old_files = find_old_docs(base_dir)
    
    if not old_files:
        print("No old documentation files found!")
        return
    
    print(f"Found {len(old_files)} old documentation files:")
    print()
    
    # Group by directory for better readability
    by_dir = {}
    for f in old_files:
        parent = f.parent.relative_to(base_dir)
        if parent not in by_dir:
            by_dir[parent] = []
        by_dir[parent].append(f.name)
    
    for parent, files in sorted(by_dir.items()):
        print(f"  {parent}/")
        for fname in sorted(files):
            print(f"    - {fname}")
    
    print()
    print("=" * 60)
    
    response = input(f"Delete these {len(old_files)} files? [y/N]: ").strip().lower()
    
    if response == 'y':
        deleted = 0
        for f in old_files:
            try:
                f.unlink()
                deleted += 1
                print(f"✓ Deleted: {f.relative_to(base_dir)}")
            except Exception as e:
                print(f"✗ Failed to delete {f.relative_to(base_dir)}: {e}")
        
        print()
        print("=" * 60)
        print(f"Deleted {deleted} of {len(old_files)} files")
    else:
        print("Cancelled - no files deleted")


if __name__ == '__main__':
    main()
