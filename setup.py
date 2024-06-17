from setuptools import setup

APP = ['typeai.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'TypeAI',
        'CFBundleDisplayName': 'TypeAI',
        'CFBundleIdentifier': 'com.rohan-jagtap.typeai',
        'CFBundleVersion': '0.1.0',
        'LSUIElement': True,
    },
    'packages': ['nltk', 'pynput', 'pyperclip'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
