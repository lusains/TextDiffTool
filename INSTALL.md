# 安装指南

## Windows系统安装指南

### 方法一：直接使用可执行文件（推荐）

1. 下载最新版本的`TextDiffTool.exe`
2. 双击运行程序，无需安装

### 方法二：从源代码运行

1. 安装Python环境
   - 访问 [Python官网](https://www.python.org/downloads/windows/)
   - 下载并安装Python 3.6或更高版本
   - 安装时勾选"Add Python to PATH"选项

2. 下载源代码
   - 下载并解压本项目的ZIP文件
   - 或使用Git克隆仓库：`git clone https://github.com/yourusername/TextDiffTool.git`

3. 安装依赖
   - 打开命令提示符(cmd)
   - 导航到项目目录：`cd path\to\TextDiffTool`
   - 安装依赖：`pip install -r src\requirements.txt`

4. 运行程序
   - 在命令提示符中执行：`python src\diff_tool.py`

### 方法三：自行打包为可执行文件

1. 完成"方法二"中的步骤1-3
2. 使用批处理文件打包
   - 双击运行`src\build_windows.bat`
   - 等待打包完成
   - 可执行文件将位于`src\dist`目录中

## 故障排除

### 常见问题

1. **运行程序时出现"python不是内部或外部命令"错误**
   - 解决方法：确保Python已正确安装并添加到系统PATH中
   - 重新安装Python，并确保勾选"Add Python to PATH"选项

2. **安装依赖时出现错误**
   - 解决方法：尝试使用管理员权限运行命令提示符
   - 命令：`pip install --user -r src\requirements.txt`

3. **程序无法启动**
   - 解决方法：检查是否安装了所有依赖
   - 尝试在命令行中运行程序以查看错误信息：`python src\diff_tool.py`

4. **打包时出现错误**
   - 解决方法：确保已安装PyInstaller
   - 命令：`pip install pyinstaller`
   - 手动运行打包命令：`pyinstaller --onefile --windowed src\diff_tool.py`

### 联系支持

如果您遇到其他问题，请通过以下方式联系我们：

- 提交GitHub Issue
- 发送邮件至：support@example.com
