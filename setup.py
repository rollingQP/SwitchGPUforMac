"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['GUI.py']
DATA_FILES = []
OPTIONS = {
        "iconfile": "Icon.icns",
        'plist': {
        'CFBundleName': "Switch GPU for Mac",
        'CFBundleDisplayName': "Switch GPU for Mac",
        'CFBundleGetInfoString': "Switch GPU for Mac GUI",
        #'CFBundleIdentifier': "com.RollingQP.osx.sandwich",
        'CFBundleVersion': "2.0.2104242006",
        'CFBundleShortVersionString': "2.0",
        'NSHumanReadableCopyright': u"Copyright 2021, RollingQP, All Rights Reserved" }
        }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
