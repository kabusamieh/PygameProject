import cx_Freeze
from cx_Freeze import *

setup(
    name = "MenuLaunch",
    options = {'build_exe':{'packages': ['pygame']}},
    executables=[
        Executable(
            "MenuLaunch.py",
            )
        ]
    )
    
