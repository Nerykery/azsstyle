# import sys
# import os
# from cx_Freeze import setup, Executable

# # ADD FILES
# files = ['icon.ico','themes/']

# # TARGET
# target = Executable(
#     script="main.py",
#     base="Win32GUI",
#     icon="icon.ico"
# )

# # SETUP CX FREEZE
# setup(
#     name = "PyDracula",
#     version = "1.0",
#     description = "Modern GUI for Python applications",
#     author = "Nerykery",
#     options = {'build_exe' : {'include_files' : files}},
#     executables = [target]
    
# )

import os
from setuptools import setup

APP = ['main.py']
DATA_FILES = []

# Автоматическое чтение зависимостей
with open('requirements.txt') as f:
    required_packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]

OPTIONS = {
    'argv_emulation': True,
    'packages': required_packages,  # Используем список из requests.txt
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

