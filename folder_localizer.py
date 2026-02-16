#!/usr/bin/env python3
"""
Win-Folder-Localizer
Set display names (or aliases) in other languages for Windows folders while 
retaining the English physical path to ensure other software functions properly.
"""

import os
import sys
import json
import argparse
import subprocess
from pathlib import Path
from typing import Dict, Optional


class FolderLocalizer:
    """Main class for localizing Windows folder display names."""
    
    def __init__(self):
        """Initialize the FolderLocalizer."""
        if sys.platform != 'win32':
            print("Warning: This tool is designed for Windows systems.")
    
    def set_localized_name(self, folder_path: str, display_name: str) -> bool:
        """
        Set a localized display name for a folder.
        
        Args:
            folder_path: Path to the folder to localize
            display_name: The display name to show in File Explorer
            
        Returns:
            True if successful, False otherwise
        """
        folder_path = os.path.abspath(folder_path)
        
        # Validate folder exists
        if not os.path.isdir(folder_path):
            print(f"Error: Folder does not exist: {folder_path}")
            return False
        
        # Create desktop.ini path
        desktop_ini_path = os.path.join(folder_path, "desktop.ini")
        
        try:
            # Create/update desktop.ini file
            self._create_desktop_ini(desktop_ini_path, display_name)
            
            # Set folder as system folder
            self._set_system_attribute(folder_path)
            
            # Set desktop.ini as system+hidden
            self._set_system_hidden_attribute(desktop_ini_path)
            
            print(f"✓ Successfully localized '{folder_path}'")
            print(f"  Display name: {display_name}")
            print(f"  Physical path remains: {folder_path}")
            print("  Note: You may need to restart Explorer to see changes.")
            
            return True
            
        except Exception as e:
            print(f"Error: Failed to localize folder: {e}")
            return False
    
    def _create_desktop_ini(self, desktop_ini_path: str, display_name: str):
        """Create or update desktop.ini file with localized name."""
        content = f"""[.ShellClassInfo]
LocalizedResourceName={display_name}
"""
        # Write as UTF-16 LE with BOM for proper Unicode support
        with open(desktop_ini_path, 'w', encoding='utf-16-le') as f:
            f.write(content)
    
    def _set_system_attribute(self, folder_path: str):
        """Set the system attribute on a folder."""
        if sys.platform == 'win32':
            subprocess.run(['attrib', '+s', folder_path], check=True, 
                         capture_output=True)
    
    def _set_system_hidden_attribute(self, file_path: str):
        """Set system and hidden attributes on a file."""
        if sys.platform == 'win32':
            subprocess.run(['attrib', '+s', '+h', file_path], check=True,
                         capture_output=True)
    
    def remove_localized_name(self, folder_path: str) -> bool:
        """
        Remove the localized display name from a folder.
        
        Args:
            folder_path: Path to the folder to restore
            
        Returns:
            True if successful, False otherwise
        """
        folder_path = os.path.abspath(folder_path)
        desktop_ini_path = os.path.join(folder_path, "desktop.ini")
        
        try:
            # Remove desktop.ini if it exists
            if os.path.exists(desktop_ini_path):
                # Remove attributes first
                if sys.platform == 'win32':
                    subprocess.run(['attrib', '-s', '-h', desktop_ini_path],
                                 capture_output=True)
                os.remove(desktop_ini_path)
            
            # Remove system attribute from folder
            if sys.platform == 'win32':
                subprocess.run(['attrib', '-s', folder_path],
                             capture_output=True)
            
            print(f"✓ Removed localized name from '{folder_path}'")
            return True
            
        except Exception as e:
            print(f"Error: Failed to remove localized name: {e}")
            return False
    
    def batch_localize(self, config_file: str) -> bool:
        """
        Localize multiple folders from a configuration file.
        
        Args:
            config_file: Path to JSON configuration file
            
        Returns:
            True if all operations successful, False otherwise
        """
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            success_count = 0
            total_count = 0
            
            for item in config.get('folders', []):
                folder_path = item.get('path')
                display_name = item.get('display_name')
                
                if not folder_path or not display_name:
                    print(f"Warning: Skipping invalid entry: {item}")
                    continue
                
                total_count += 1
                # Expand environment variables
                folder_path = os.path.expandvars(folder_path)
                
                if self.set_localized_name(folder_path, display_name):
                    success_count += 1
                print()  # Blank line for readability
            
            print(f"Batch operation complete: {success_count}/{total_count} successful")
            return success_count == total_count
            
        except Exception as e:
            print(f"Error: Failed to process config file: {e}")
            return False
    
    def list_localized_folders(self, root_path: str):
        """
        List all folders with localized names in a directory tree.
        
        Args:
            root_path: Root directory to search
        """
        root_path = os.path.abspath(root_path)
        found_count = 0
        
        print(f"Searching for localized folders in: {root_path}\n")
        
        for dirpath, dirnames, filenames in os.walk(root_path):
            if 'desktop.ini' in filenames:
                desktop_ini_path = os.path.join(dirpath, 'desktop.ini')
                try:
                    # Try to read the desktop.ini file
                    with open(desktop_ini_path, 'r', encoding='utf-16-le') as f:
                        content = f.read()
                    
                    # Check if it has LocalizedResourceName
                    if 'LocalizedResourceName=' in content:
                        for line in content.split('\n'):
                            if line.startswith('LocalizedResourceName='):
                                display_name = line.split('=', 1)[1].strip()
                                print(f"Folder: {dirpath}")
                                print(f"  Display Name: {display_name}\n")
                                found_count += 1
                                break
                except Exception as e:
                    # Skip folders we can't read
                    pass
        
        print(f"Found {found_count} localized folder(s)")


def main():
    """Main entry point for the command-line interface."""
    parser = argparse.ArgumentParser(
        description='Set display names for Windows folders while keeping English paths',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Localize a single folder
  python folder_localizer.py --set "C:\\Users\\John\\Documents" --name "文档"
  
  # Localize multiple folders from a config file
  python folder_localizer.py --batch config.json
  
  # Remove localized name
  python folder_localizer.py --remove "C:\\Users\\John\\Documents"
  
  # List all localized folders
  python folder_localizer.py --list "C:\\Users\\John"
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--set', metavar='FOLDER', 
                      help='Folder path to localize')
    group.add_argument('--batch', metavar='CONFIG',
                      help='JSON config file for batch localization')
    group.add_argument('--remove', metavar='FOLDER',
                      help='Remove localized name from folder')
    group.add_argument('--list', metavar='ROOT',
                      help='List all localized folders in directory tree')
    
    parser.add_argument('--name', metavar='DISPLAY_NAME',
                       help='Display name for the folder (required with --set)')
    
    args = parser.parse_args()
    
    localizer = FolderLocalizer()
    
    if args.set:
        if not args.name:
            parser.error("--name is required when using --set")
        success = localizer.set_localized_name(args.set, args.name)
        sys.exit(0 if success else 1)
    
    elif args.batch:
        success = localizer.batch_localize(args.batch)
        sys.exit(0 if success else 1)
    
    elif args.remove:
        success = localizer.remove_localized_name(args.remove)
        sys.exit(0 if success else 1)
    
    elif args.list:
        localizer.list_localized_folders(args.list)
        sys.exit(0)


if __name__ == '__main__':
    main()
