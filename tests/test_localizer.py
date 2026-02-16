#!/usr/bin/env python3
"""
Test script for Win-Folder-Localizer
This script demonstrates the functionality without requiring Windows.
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

# Add parent directory to path to import folder_localizer
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from folder_localizer import FolderLocalizer


def test_desktop_ini_creation():
    """Test that desktop.ini files are created correctly."""
    print("Test 1: Desktop.ini File Creation")
    print("-" * 50)
    
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        test_folder = os.path.join(tmpdir, "TestFolder")
        os.makedirs(test_folder)
        
        localizer = FolderLocalizer()
        
        # Create desktop.ini (without Windows-specific attributes)
        desktop_ini_path = os.path.join(test_folder, "desktop.ini")
        localizer._create_desktop_ini(desktop_ini_path, "测试文件夹")
        
        # Verify file was created
        assert os.path.exists(desktop_ini_path), "desktop.ini should exist"
        
        # Read and verify content
        with open(desktop_ini_path, 'r', encoding='utf-16-le') as f:
            content = f.read()
        
        assert "[.ShellClassInfo]" in content, "Should contain .ShellClassInfo section"
        assert "LocalizedResourceName=测试文件夹" in content, "Should contain localized name"
        
        print("✓ desktop.ini created successfully")
        print(f"  Content preview: {content[:100]}...")
        print()


def test_config_file_parsing():
    """Test that configuration files can be parsed."""
    print("Test 2: Configuration File Parsing")
    print("-" * 50)
    
    import json
    
    # Test with Chinese config
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'examples', 'config_chinese.json'
    )
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    assert 'folders' in config, "Config should have 'folders' key"
    assert len(config['folders']) > 0, "Config should have at least one folder"
    
    print(f"✓ Successfully parsed {config_path}")
    print(f"  Description: {config.get('description', 'N/A')}")
    print(f"  Number of folders: {len(config['folders'])}")
    print(f"  Sample folder: {config['folders'][0]}")
    print()


def test_cli_help():
    """Test that CLI help works."""
    print("Test 3: CLI Help Display")
    print("-" * 50)
    
    import subprocess
    
    script_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'folder_localizer.py'
    )
    
    result = subprocess.run(
        [sys.executable, script_path, '--help'],
        capture_output=True,
        text=True
    )
    
    assert result.returncode == 0, "Help command should succeed"
    assert '--set' in result.stdout, "Help should mention --set option"
    assert '--batch' in result.stdout, "Help should mention --batch option"
    assert '--remove' in result.stdout, "Help should mention --remove option"
    assert '--list' in result.stdout, "Help should mention --list option"
    
    print("✓ CLI help displays correctly")
    print(f"  Sample output: {result.stdout[:200]}...")
    print()


def test_all_example_configs():
    """Test that all example configurations are valid JSON."""
    print("Test 4: Example Configuration Files")
    print("-" * 50)
    
    import json
    
    examples_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'examples'
    )
    
    configs = [
        'config_chinese.json',
        'config_japanese.json',
        'config_spanish.json',
        'config_french.json',
        'config_german.json'
    ]
    
    for config_file in configs:
        config_path = os.path.join(examples_dir, config_file)
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        assert 'folders' in config, f"{config_file} should have 'folders' key"
        print(f"✓ {config_file}: {len(config['folders'])} folders, {config.get('description', 'N/A')}")
    
    print()


def test_unicode_support():
    """Test that Unicode characters are properly handled."""
    print("Test 5: Unicode Character Support")
    print("-" * 50)
    
    test_names = [
        ("Chinese", "文档"),
        ("Japanese", "ドキュメント"),
        ("Spanish", "Documentos"),
        ("French", "Téléchargements"),
        ("German", "Dokumente"),
        ("Russian", "Документы"),
        ("Arabic", "المستندات"),
        ("Korean", "문서"),
    ]
    
    with tempfile.TemporaryDirectory() as tmpdir:
        localizer = FolderLocalizer()
        
        for lang, name in test_names:
            test_file = os.path.join(tmpdir, f"test_{lang}.ini")
            localizer._create_desktop_ini(test_file, name)
            
            # Read back and verify
            with open(test_file, 'r', encoding='utf-16-le') as f:
                content = f.read()
            
            assert name in content, f"{lang} characters should be preserved"
            print(f"✓ {lang}: {name}")
    
    print()


def main():
    """Run all tests."""
    print("=" * 50)
    print("Win-Folder-Localizer Test Suite")
    print("=" * 50)
    print()
    
    try:
        test_desktop_ini_creation()
        test_config_file_parsing()
        test_cli_help()
        test_all_example_configs()
        test_unicode_support()
        
        print("=" * 50)
        print("All tests passed! ✓")
        print("=" * 50)
        print()
        print("Note: These are unit tests for the core functionality.")
        print("Full integration testing requires a Windows environment.")
        print()
        
        return 0
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
