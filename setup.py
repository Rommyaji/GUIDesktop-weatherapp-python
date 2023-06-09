import cx_Freeze

executables = [cx_Freeze.Executable("weather_display.py")]

cx_Freeze.setup(
    name="Weather App",
    options={"build_exe": {"packages":["tkinter","requests"],"include_files":["icon.ico"]}},
    executables = executables
    )
