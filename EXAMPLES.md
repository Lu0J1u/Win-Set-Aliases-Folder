# Usage Examples

This document provides detailed examples of using Win-Folder-Localizer for various scenarios.

## Table of Contents
- [Single Folder Localization](#single-folder-localization)
- [Batch Localization](#batch-localization)
- [Removing Localization](#removing-localization)
- [Finding Localized Folders](#finding-localized-folders)
- [Custom Configurations](#custom-configurations)
- [Common Scenarios](#common-scenarios)

## Single Folder Localization

### Example 1: Localize Documents Folder to Chinese

```bash
python folder_localizer.py --set "%USERPROFILE%\Documents" --name "文档"
```

**Output**:
```
✓ Successfully localized 'C:\Users\John\Documents'
  Display name: 文档
  Physical path remains: C:\Users\John\Documents
  Note: You may need to restart Explorer to see changes.
```

**Before**: Documents  
**After**: 文档 (in File Explorer)  
**Path**: Still `C:\Users\John\Documents`

### Example 2: Localize Downloads Folder to Japanese

```bash
python folder_localizer.py --set "%USERPROFILE%\Downloads" --name "ダウンロード"
```

### Example 3: Localize a Project Folder to Spanish

```bash
python folder_localizer.py --set "C:\Projects\WebApp" --name "Aplicación Web"
```

## Batch Localization

### Example 4: Localize All User Folders to Chinese

```bash
python folder_localizer.py --batch examples/config_chinese.json
```

**Output**:
```
✓ Successfully localized 'C:\Users\John\Documents'
  Display name: 文档
  Physical path remains: C:\Users\John\Documents
  Note: You may need to restart Explorer to see changes.

✓ Successfully localized 'C:\Users\John\Downloads'
  Display name: 下载
  Physical path remains: C:\Users\John\Downloads
  Note: You may need to restart Explorer to see changes.

... (more folders) ...

Batch operation complete: 6/6 successful
```

### Example 5: Use Different Language Presets

```bash
# Japanese
python folder_localizer.py --batch examples/config_japanese.json

# Spanish
python folder_localizer.py --batch examples/config_spanish.json

# French
python folder_localizer.py --batch examples/config_french.json

# German
python folder_localizer.py --batch examples/config_german.json
```

## Removing Localization

### Example 6: Remove Localization from a Single Folder

```bash
python folder_localizer.py --remove "%USERPROFILE%\Documents"
```

**Output**:
```
✓ Removed localized name from 'C:\Users\John\Documents'
```

**Result**: Folder returns to displaying "Documents" in File Explorer.

### Example 7: Remove Localization from Multiple Folders

```bash
# Remove from Documents
python folder_localizer.py --remove "%USERPROFILE%\Documents"

# Remove from Downloads
python folder_localizer.py --remove "%USERPROFILE%\Downloads"

# Remove from Pictures
python folder_localizer.py --remove "%USERPROFILE%\Pictures"
```

## Finding Localized Folders

### Example 8: List All Localized Folders in User Directory

```bash
python folder_localizer.py --list "%USERPROFILE%"
```

**Output**:
```
Searching for localized folders in: C:\Users\John

Folder: C:\Users\John\Documents
  Display Name: 文档

Folder: C:\Users\John\Downloads
  Display Name: 下载

Folder: C:\Users\John\Pictures
  Display Name: 图片

Found 3 localized folder(s)
```

### Example 9: List Localized Folders in a Specific Directory

```bash
python folder_localizer.py --list "C:\Projects"
```

## Custom Configurations

### Example 10: Create a Custom Configuration for Your Needs

Create a file named `my_config.json`:

```json
{
  "description": "My custom folder localization",
  "folders": [
    {
      "path": "C:\\Projects\\WebApp",
      "display_name": "网站应用"
    },
    {
      "path": "C:\\Projects\\MobileApp",
      "display_name": "移动应用"
    },
    {
      "path": "%USERPROFILE%\\Work",
      "display_name": "工作"
    }
  ]
}
```

Then run:
```bash
python folder_localizer.py --batch my_config.json
```

### Example 11: Mix Languages in Custom Configuration

```json
{
  "description": "Mixed language configuration",
  "folders": [
    {
      "path": "%USERPROFILE%\\Documents",
      "display_name": "文档"
    },
    {
      "path": "%USERPROFILE%\\Downloads",
      "display_name": "Téléchargements"
    },
    {
      "path": "%USERPROFILE%\\Pictures",
      "display_name": "Bilder"
    }
  ]
}
```

## Common Scenarios

### Scenario 1: You Want Chinese Interface but Keep English Paths

**Problem**: You use software that expects English folder names (e.g., OneDrive, Dropbox, development tools), but you want File Explorer to show Chinese names.

**Solution**: Use Win-Folder-Localizer!

```bash
python folder_localizer.py --batch examples/config_chinese.json
```

**Result**:
- File Explorer shows: 文档, 下载, 图片
- Software still sees: Documents, Downloads, Pictures
- All file paths remain unchanged

### Scenario 2: Multilingual Team with Shared Network Drives

**Problem**: Team members speak different languages but need to access the same shared folders.

**Solution**: Each user can localize their local folders while shared paths remain the same.

```bash
# User 1 (Chinese speaker)
python folder_localizer.py --set "C:\SharedProjects\Reports" --name "报告"

# User 2 (Japanese speaker)  
python folder_localizer.py --set "C:\SharedProjects\Reports" --name "レポート"
```

**Result**: Each user sees folder names in their language, but all refer to the same path.

### Scenario 3: Testing Before Full Deployment

**Problem**: You want to test localization on one folder before applying to all.

**Solution**: Start with a single folder, verify it works, then use batch.

```bash
# Step 1: Test with Documents folder
python folder_localizer.py --set "%USERPROFILE%\Documents" --name "文档"

# Step 2: Restart Explorer and verify

# Step 3: If satisfied, apply to all folders
python folder_localizer.py --batch examples/config_chinese.json
```

### Scenario 4: Temporary Localization for Demonstration

**Problem**: You need to show a localized interface for a demo but want to revert afterward.

**Solution**: Localize, do the demo, then remove.

```bash
# Before demo
python folder_localizer.py --batch examples/config_japanese.json

# ... do your demo ...

# After demo  
python folder_localizer.py --remove "%USERPROFILE%\Documents"
python folder_localizer.py --remove "%USERPROFILE%\Downloads"
# etc.
```

## Programmatic Usage Examples

### Example 12: Using the Python API

```python
from folder_localizer import FolderLocalizer

# Create localizer instance
localizer = FolderLocalizer()

# Localize single folder
localizer.set_localized_name(r"C:\Users\John\Documents", "文档")

# Batch localize from config
localizer.batch_localize("examples/config_chinese.json")

# List localized folders
localizer.list_localized_folders(r"C:\Users\John")

# Remove localization
localizer.remove_localized_name(r"C:\Users\John\Documents")
```

### Example 13: Integration in a Setup Script

```python
#!/usr/bin/env python3
"""Setup script to configure user environment."""

from folder_localizer import FolderLocalizer
import os

def setup_user_folders(language='chinese'):
    """Set up user folders with localized names."""
    
    localizer = FolderLocalizer()
    config_file = f"examples/config_{language}.json"
    
    if os.path.exists(config_file):
        print(f"Setting up folders with {language} localization...")
        success = localizer.batch_localize(config_file)
        
        if success:
            print("✓ Setup complete!")
            print("Please restart Windows Explorer to see changes.")
        else:
            print("❌ Setup failed. Please check the logs.")
    else:
        print(f"Error: Configuration file not found: {config_file}")

if __name__ == '__main__':
    setup_user_folders('chinese')
```

## Tips and Best Practices

1. **Always test on a single folder first** before batch processing
2. **Keep a backup** of your configuration files
3. **Document your changes** - note which folders you've localized
4. **Restart Explorer** after making changes for them to take effect
5. **Use environment variables** (`%USERPROFILE%`) in configs for portability
6. **Verify software compatibility** with critical applications before full deployment

## Troubleshooting Examples

### Issue: Changes not visible
```bash
# Solution 1: Check if folder was actually localized
python folder_localizer.py --list "%USERPROFILE%"

# Solution 2: Try localizing again
python folder_localizer.py --set "%USERPROFILE%\Documents" --name "文档"
```

### Issue: Want to revert all changes
```bash
# Step 1: Find all localized folders
python folder_localizer.py --list "%USERPROFILE%"

# Step 2: Remove localization from each found folder
python folder_localizer.py --remove "path\to\folder1"
python folder_localizer.py --remove "path\to\folder2"
```

## Further Reading

- [README.md](README.md) - Full documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [examples/README.md](examples/README.md) - Configuration examples
