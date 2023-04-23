from cx_Freeze import setup, Executable

setup(
    name="MyProgram",
    version="1.0",
    description="My PyQt5 program",
    executables=[Executable("main.py", base="Win32GUI")],
    options={
        "build_exe": {
            "include_files": ["Calc_Library.py", "Newdesign.py", "docs", "icons", "Rubik", "files_rc.py"],
            "packages": ["PySide6", "keyboard", "typing", "decimal", "importlib", "sys", "os"],
            "include_msvcr": True,
        }
    },
)