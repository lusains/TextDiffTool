# 文本差异比较工具 (TextDiffTool)

一个简单易用的文本差异比较工具，可以直观地展示两个文本文件之间的差异。该工具使用Python和PyQt5开发，支持Windows系统。

[English](README.md) | 中文

## 功能特点

- 并排显示两个文本文件的内容
- 高亮显示文件之间的差异（添加、删除、修改）
- 支持通过快捷键快速导航到下一个/上一个差异
- 简洁直观的用户界面
- 支持所有文本文件格式

## 安装方法

### 方法一：使用可执行文件（推荐普通用户）

1. 从[发布页面](https://github.com/yourusername/TextDiffTool/releases)下载最新的`TextDiffTool.exe`文件
2. 双击运行即可，无需安装

### 方法二：从源代码安装（推荐开发者）

#### 前提条件

- Python 3.6 或更高版本
- pip（Python包管理器）

#### 安装步骤

1. 克隆或下载此仓库到本地
   ```
   git clone https://github.com/yourusername/TextDiffTool.git
   cd TextDiffTool
   ```

2. 安装依赖项
   ```
   pip install -r src/requirements.txt
   ```

3. 运行程序
   ```
   python src/diff_tool.py
   ```

### 方法三：打包为可执行文件

如果您想自己打包为可执行文件，可以使用以下两种方法之一：

#### 使用PyInstaller

```
pip install pyinstaller
cd src
pyinstaller --onefile --windowed --icon=icon.ico diff_tool.py
```

打包后的可执行文件将位于`dist`目录中。

#### 使用cx_Freeze

```
pip install cx_Freeze
cd src
python setup.py build
```

打包后的文件将位于`build`目录中。

## 使用方法

1. 启动程序
2. 点击"选择文件1"按钮，选择第一个要比较的文本文件
3. 点击"选择文件2"按钮，选择第二个要比较的文本文件
4. 点击"比较差异"按钮，查看两个文件的差异
5. 使用"下一个差异"和"上一个差异"按钮（或快捷键）在差异之间导航

### 快捷键

- `Ctrl+O` - 打开文件1
- `Ctrl+P` - 打开文件2
- `Ctrl+D` - 比较差异
- `F3` - 跳转到下一个差异
- `Shift+F3` - 跳转到上一个差异

## 差异显示说明

- **绿色背景**：表示在文件2中添加的内容（相对于文件1）
- **红色背景**：表示在文件1中存在但在文件2中删除的内容
- **黄色背景**：表示内容被修改

## 系统要求

- 操作系统：Windows 7/8/10/11
- 屏幕分辨率：最低 1024x768
- 内存：至少 4GB RAM

## 常见问题

**Q: 为什么有些文件无法正确显示？**  
A: 该工具默认使用UTF-8编码读取文件。如果文件使用其他编码（如GBK、ANSI等），可能会出现乱码。

**Q: 如何比较大型文件？**  
A: 该工具适合比较中小型文本文件。对于非常大的文件（>10MB），可能会导致性能下降。

## 许可证

MIT License

## 贡献

欢迎提交问题报告和功能请求！如果您想贡献代码，请先创建一个issue讨论您想要更改的内容。
