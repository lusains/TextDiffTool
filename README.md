# Text Difference Tool (TextDiffTool)

A simple and easy-to-use text difference comparison tool that visually displays the differences between two text files. This tool is developed using Python and PyQt5, and supports Windows systems.

English | [中文](README_CN.md)

## Features

- Side-by-side display of two text files
- Highlighted differences between files (additions, deletions, modifications)
- Quick navigation to next/previous difference using keyboard shortcuts
- Clean and intuitive user interface
- Support for all text file formats

## Installation

### Method 1: Using the Executable File (Recommended for Regular Users)

1. Download the latest `TextDiffTool.exe` file from the [releases page](https://github.com/lusains/TextDiffTool/releases)
2. Double-click to run, no installation required

### Method 2: Install from Source Code (Recommended for Developers)

#### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

#### Installation Steps

1. Clone or download this repository to your local machine
   ```
   git clone https://github.com/lusains/TextDiffTool.git
   cd TextDiffTool
   ```

2. Install dependencies
   ```
   pip install -r src/requirements.txt
   ```

3. Run the program
   ```
   python src/diff_tool.py
   ```

### Method 3: Package as an Executable File

If you want to package it as an executable file yourself, you can use one of the following two methods:

#### Using PyInstaller

```
pip install pyinstaller
cd src
pyinstaller --onefile --windowed --icon=icon.ico diff_tool.py
```

The packaged executable will be located in the `dist` directory.

#### Using cx_Freeze

```
pip install cx_Freeze
cd src
python setup.py build
```

The packaged files will be located in the `build` directory.

## Usage

1. Start the program
2. Click the "Select File 1" button to choose the first text file to compare
3. Click the "Select File 2" button to choose the second text file to compare
4. Click the "Compare Differences" button to view the differences between the two files
5. Use the "Next Difference" and "Previous Difference" buttons (or keyboard shortcuts) to navigate between differences

### Keyboard Shortcuts

- `Ctrl+O` - Open File 1
- `Ctrl+P` - Open File 2
- `Ctrl+D` - Compare Differences
- `F3` - Jump to next difference
- `Shift+F3` - Jump to previous difference

## Difference Display Legend

- **Green background**: Indicates content added in file 2 (relative to file 1)
- **Red background**: Indicates content that exists in file 1 but was deleted in file 2
- **Yellow background**: Indicates content that was modified

## System Requirements

- Operating System: Windows 7/8/10/11
- Screen Resolution: Minimum 1024x768
- Memory: At least 4GB RAM

## FAQ

**Q: Why can't some files display correctly?**  
A: This tool uses UTF-8 encoding to read files by default. If the file uses other encodings (such as GBK, ANSI, etc.), garbled characters may appear.

**Q: How to compare large files?**  
A: This tool is suitable for comparing small to medium-sized text files. For very large files (>10MB), performance may decrease.

## License

MIT License

## Contributions

Bug reports and feature requests are welcome! If you want to contribute code, please create an issue first to discuss what you would like to change.
