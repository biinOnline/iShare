import requests
from cx_Freeze import setup, Executable
import sys, os
from idna import idnadata
from multiprocessing import Queue
import os

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

sys.argv.append("build")
filename="iStock.py"
icon= "is_icon.ico"

base = None

options={
        "build_exe": {
            "packages": ["idna"],
            },
        },

if sys.platform=="win64":
    base="Win64GUI"

exe = Executable(script='iStock.py', base = base, icon='is_icon.ico')

additional_mods = ['numpy.core._methods', 'numpy.lib.format']
additional_packages = ['asyncio', 'asyncio.compat', 'appdirs', 'pkg_resources._vendor', 'tkinter']

setup(
    name = "iShare compiles real-time market data.",
    version = "1.2.0.1",
    description = 'iShare: Market Data.',
    author = 'wakili.ai',
    options = {
        'build_exe': {
            'includes': additional_mods,
            'packages': additional_packages,
            'include_files':[
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                ],
            
        }},
    executables=[exe])


