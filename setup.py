from setuptools import setup

APP = ['wxbutton.py']
APP_NAME = 'wxButton'
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['wx']
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
