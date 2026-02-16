# Quick Start Guide

Get started with Win-Folder-Localizer in 5 minutes!

## Prerequisites

- Windows 7 or later
- Python 3.6 or later installed

## Installation

1. Download or clone the repository:
   ```bash
   git clone https://github.com/Lu0J1u/Win-Folder-Localizer.git
   cd Win-Folder-Localizer
   ```

2. No additional installation needed! The tool uses only Python standard library.

## Basic Usage

### Example 1: Localize Your Documents Folder to Chinese

```bash
python folder_localizer.py --set "%USERPROFILE%\Documents" --name "文档"
```

**Result**: Your Documents folder will display as "文档" in File Explorer, but the path remains `C:\Users\YourName\Documents`.

### Example 2: Batch Localize All User Folders to Japanese

```bash
python folder_localizer.py --batch examples/config_japanese.json
```

**Result**: All common user folders (Documents, Downloads, Pictures, etc.) will display in Japanese.

### Example 3: Remove Localization

```bash
python folder_localizer.py --remove "%USERPROFILE%\Documents"
```

**Result**: The Documents folder returns to its original display name.

## Available Pre-configured Languages

Choose from these ready-to-use configurations:

| Language | Config File | Example |
|----------|-------------|---------|
| Chinese (Simplified) | `examples/config_chinese.json` | 文档, 下载, 图片 |
| Japanese | `examples/config_japanese.json` | ドキュメント, ダウンロード |
| Spanish | `examples/config_spanish.json` | Documentos, Descargas |
| French | `examples/config_french.json` | Documents, Téléchargements |
| German | `examples/config_german.json` | Dokumente, Downloads |

## Important Notes

1. **Administrator Rights**: May be required for some system folders
2. **Restart Explorer**: After localizing, restart Windows Explorer to see changes:
   - Press `Ctrl+Shift+Esc`, find "Windows Explorer", right-click → Restart
3. **Physical Path Unchanged**: All software will continue to access folders by their English paths

## Custom Configuration

Create your own `config.json`:

```json
{
  "folders": [
    {
      "path": "C:\\MyFolder",
      "display_name": "My Localized Name"
    }
  ]
}
```

Then run:
```bash
python folder_localizer.py --batch config.json
```

## Getting Help

```bash
python folder_localizer.py --help
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check the [examples/](examples/) directory for more language templates
- Create custom configurations for your specific needs

## Troubleshooting

**Problem**: Changes don't appear in File Explorer
- **Solution**: Restart Windows Explorer (see step 2 above)

**Problem**: Permission denied error
- **Solution**: Run Command Prompt or PowerShell as Administrator

**Problem**: desktop.ini file is visible
- **Solution**: Ensure "Show hidden files" is disabled in File Explorer settings

For more help, see the main [README.md](README.md) or open an issue on GitHub.
