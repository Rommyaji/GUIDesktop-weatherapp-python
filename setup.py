import cx_Freeze

executables = [cx_Freeze.Executable("main.py", icon="icon.ico")]

cx_Freeze.setup(
    name="Weather App",
    options={
        "build_exe": {
            "packages":["tkinter","requests"],
        }
    },
    executables = executables
)
