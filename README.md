# Win-Folder-Localizer

Set display names (or aliases) in other languages for Windows folders while retaining the English physical path to ensure other software functions properly.

## Overview

Win-Folder-Localizer is a Python tool that allows you to set localized display names for Windows folders without changing their physical path names. This is useful when you want your folders to appear in your native language in File Explorer while maintaining English paths for compatibility with software that expects specific folder names.

### Key Features

- ✅ **Localized Display Names**: Show folder names in any language in Windows File Explorer
- ✅ **Preserved Physical Paths**: Keep original English folder paths unchanged for software compatibility
- ✅ **Batch Processing**: Localize multiple folders at once using JSON configuration files
- ✅ **Easy Reversion**: Remove localized names and restore original display
- ✅ **Discovery Tool**: List all localized folders in a directory tree

### How It Works

The tool uses Windows' built-in folder customization feature through `desktop.ini` files. It:
1. Creates a `desktop.ini` file with `LocalizedResourceName` entry in the target folder
2. Sets the folder as a system folder (required by Windows)
3. Hides the `desktop.ini` file

The folder will display the localized name in File Explorer, but all file paths, command-line access, and API calls continue to use the original English path.

## Requirements

- **Operating System**: Windows 7 or later
- **Python**: Python 3.6 or later
- **Permissions**: Administrator privileges may be required for some system folders

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/Lu0J1u/Win-Folder-Localizer.git
   cd Win-Folder-Localizer
   ```

2. No additional dependencies required - uses only Python standard library.

## Usage

### Command-Line Interface

#### Localize a Single Folder

Set a localized display name for a specific folder:

```bash
python folder_localizer.py --set "C:\Users\John\Documents" --name "文档"
```

**Example**: Localize Documents folder to Chinese:
```bash
python folder_localizer.py --set "%USERPROFILE%\Documents" --name "文档"
```

**Example**: Localize Downloads folder to Japanese:
```bash
python folder_localizer.py --set "%USERPROFILE%\Downloads" --name "ダウンロード"
```

#### Batch Localization

Localize multiple folders at once using a JSON configuration file:

```bash
python folder_localizer.py --batch examples/config_chinese.json
```

See the `examples/` directory for pre-configured language templates.

#### Remove Localized Name

Restore the original folder display name:

```bash
python folder_localizer.py --remove "C:\Users\John\Documents"
```

#### List Localized Folders

Find all folders with localized names in a directory tree:

```bash
python folder_localizer.py --list "C:\Users\John"
```

### Configuration File Format

Create a JSON file with the following structure:

```json
{
  "description": "Optional description of this configuration",
  "folders": [
    {
      "path": "%USERPROFILE%\\Documents",
      "display_name": "文档"
    },
    {
      "path": "%USERPROFILE%\\Downloads",
      "display_name": "下载"
    }
  ]
}
```

**Notes**:
- Use `%USERPROFILE%` or other environment variables - they will be expanded automatically
- Use double backslashes (`\\`) in JSON for Windows paths
- Use UTF-8 encoding for the JSON file to support Unicode characters

### Programmatic Usage

You can also use the `FolderLocalizer` class in your Python code:

```python
from folder_localizer import FolderLocalizer

localizer = FolderLocalizer()

# Localize a single folder
localizer.set_localized_name(r"C:\Users\John\Documents", "文档")

# Batch localization
localizer.batch_localize("config.json")

# Remove localization
localizer.remove_localized_name(r"C:\Users\John\Documents")

# List localized folders
localizer.list_localized_folders(r"C:\Users\John")
```

## Examples

The `examples/` directory contains pre-configured templates for common languages:

- `config_chinese.json` - Chinese (Simplified) 简体中文
- `config_japanese.json` - Japanese 日本語
- `config_spanish.json` - Spanish Español
- `config_french.json` - French Français
- `config_german.json` - German Deutsch

### Common Use Cases

#### Localize User Folders to Chinese
```bash
python folder_localizer.py --batch examples/config_chinese.json
```

#### Localize a Project Folder
```bash
python folder_localizer.py --set "C:\Projects\MyProject" --name "我的项目"
```

#### Restore All Folders in User Directory
```bash
# First, list all localized folders
python folder_localizer.py --list "%USERPROFILE%"

# Then remove localization from each folder
python folder_localizer.py --remove "%USERPROFILE%\Documents"
python folder_localizer.py --remove "%USERPROFILE%\Downloads"
# ... etc
```

## Important Notes

### Windows Explorer Refresh

After localizing folders, you may need to restart Windows Explorer to see the changes:

1. **Method 1**: Press `Ctrl+Shift+Esc` to open Task Manager, find "Windows Explorer", right-click and select "Restart"
2. **Method 2**: Log out and log back in
3. **Method 3**: Restart your computer

### Compatibility

- ✅ **Works with**: All file operations, command-line tools, and software that access folders by path
- ✅ **Preserves**: Shortcuts, symbolic links, and junction points
- ⚠️ **Known Issue**: Windows Update KB5074109 (January 2026) may break `LocalizedResourceName` on some systems

### Limitations

- Only works on Windows systems
- Requires proper Windows Explorer to display localized names
- Some system folders may be protected and require administrator privileges
- Third-party file managers may not respect localized names

### Security Considerations

- The tool modifies folder attributes and creates system files
- Always backup important data before making system changes
- Review configuration files before batch processing
- Administrator privileges may expose additional system folders

## Troubleshooting

### Localized names don't appear in File Explorer

1. Restart Windows Explorer (see "Windows Explorer Refresh" above)
2. Verify the folder has the system attribute: `attrib "C:\Path\To\Folder"`
3. Check if `desktop.ini` exists and has correct attributes
4. Ensure `desktop.ini` is saved in UTF-16 LE encoding

### Permission denied errors

- Run the command prompt or PowerShell as Administrator
- Some system folders are protected and may not be localizable

### desktop.ini is visible in File Explorer

- Ensure "Show hidden files" is disabled in File Explorer settings
- Verify the file has system + hidden attributes: `attrib "C:\Path\To\Folder\desktop.ini"`

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

### Ideas for Contributions

- Additional language configuration templates
- GUI interface for easier use
- Integration with Windows context menu
- Support for custom folder icons
- Automated backup/restore functionality

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

This tool uses Windows' built-in folder customization features as documented in Microsoft's [How to Customize Folders with Desktop.ini](https://learn.microsoft.com/en-us/windows/win32/shell/how-to-customize-folders-with-desktop-ini) guide.

## Author

Created by [Lu0J1u](https://github.com/Lu0J1u)

---

**Disclaimer**: This tool modifies Windows folder attributes and creates system files. While it uses standard Windows features, always backup important data and test on non-critical folders first. The authors are not responsible for any data loss or system issues.
