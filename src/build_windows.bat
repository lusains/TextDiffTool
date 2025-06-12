@echo off
echo 正在构建文本差异比较工具...

REM 确保已安装所需依赖
pip install -r requirements.txt
pip install pyinstaller

REM 使用PyInstaller打包
pyinstaller --onefile --windowed --icon=icon.ico --name=TextDiffTool diff_tool.py

echo 构建完成！可执行文件位于dist目录中。
pause
