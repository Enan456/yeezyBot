from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("AutoCheckout.py", base=base)]

packages = ['json', 'time', 'httplib2', 'lxml', 'requests', 'bs4', 'configparser',
            're', 'lxml', 'requests', 'time', 'datetime', 'webbrowser', 'selenium']
options = {
    'build_exe': {

        'packages': packages,
    },

}

setup(
    name="YeezyBot",
    options=options,
    version='1.01',
    description='AutoCopYeezyBot',
    executables=executables
)
