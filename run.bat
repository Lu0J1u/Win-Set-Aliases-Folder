@echo off
chcp 936 >nul

echo.

attrib -s -h -r desktop.ini 2>nul

set /p newName=Please enter the new name for the folder: 

echo [.ShellClassInfo] > desktop.ini
echo LocalizedResourceName=%newName% >> desktop.ini

attrib +s +h desktop.ini

cd ..

for %%I in ("%~dp0.") do set "CurrentFolder=%%~nxI"


attrib -r "%CurrentFolder%"
timeout /t 1 /nobreak >nul
attrib +r "%CurrentFolder%"

echo Force restart explorer.exe to apply changes...
taskkill /f /im explorer.exe >nul

echo Restarting explorer.exe...
start explorer.exe

start "" "%~dp0"

echo.
echo --- Rename Complete ---
echo Folder "%CurrentFolder%" has been renamed to "%newName%"
pause