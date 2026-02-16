# Configuration Examples

This directory contains pre-configured JSON templates for localizing Windows folders to various languages.

## Available Languages

- **Chinese (Simplified)**: `config_chinese.json` - 简体中文
- **Japanese**: `config_japanese.json` - 日本語  
- **Spanish**: `config_spanish.json` - Español
- **French**: `config_french.json` - Français
- **German**: `config_german.json` - Deutsch

## Usage

Use any of these configuration files with the batch localization feature:

```bash
python folder_localizer.py --batch examples/config_chinese.json
```

## Customization

You can modify these files or create your own by following this structure:

```json
{
  "description": "Description of this configuration",
  "folders": [
    {
      "path": "%USERPROFILE%\\FolderName",
      "display_name": "Display Name in Your Language"
    }
  ]
}
```

### Tips

- Use environment variables like `%USERPROFILE%` for portability
- Use double backslashes (`\\`) for Windows paths in JSON
- Save files as UTF-8 to support Unicode characters
- Test with a single folder before batch processing

## Common Folder Paths

Here are some common Windows user folder paths you can localize:

- `%USERPROFILE%\Desktop` - Desktop folder
- `%USERPROFILE%\Documents` - Documents folder
- `%USERPROFILE%\Downloads` - Downloads folder
- `%USERPROFILE%\Pictures` - Pictures folder
- `%USERPROFILE%\Videos` - Videos folder
- `%USERPROFILE%\Music` - Music folder
- `%USERPROFILE%\OneDrive` - OneDrive folder
- `%PUBLIC%\Public Documents` - Public Documents folder

## Creating New Language Templates

To create a template for a new language:

1. Copy one of the existing configuration files
2. Rename it appropriately (e.g., `config_italian.json`)
3. Update the `description` field
4. Replace the `display_name` values with translations in your target language
5. Test with a single folder first

## Contributing

If you create a configuration for a new language, please consider contributing it back to the project!
