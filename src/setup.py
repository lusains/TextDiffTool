import sys
from cx_Freeze import setup, Executable

# 依赖项
build_exe_options = {
    "packages": ["os", "sys", "difflib", "PyQt5"],
    "excludes": [],
    "include_files": []
}

# 基本信息
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="TextDiffTool",
    version="1.0.0",
    description="文本差异比较工具",
    options={"build_exe": build_exe_options},
    executables=[Executable("diff_tool.py", base=base, target_name="TextDiffTool.exe")]
)
