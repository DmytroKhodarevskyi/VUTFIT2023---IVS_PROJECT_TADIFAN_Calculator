from cx_Freeze import setup, Executable

setup(
    name="MyProgram",
    version="1.0",
    description="My PyQt5 program",
    executables=[Executable("main.py")],
    options={
        "build_exe": {
            "include_files": ["Calc_Library.py", "Newdesign.py"],
            "packages": ["PySide6.QtWidgets", "keyboard", "typing"],
            "include_msvcr": True,
        }
    },
)