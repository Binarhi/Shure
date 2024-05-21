from setuptools import setup

APP =['MAin_M32_Shure.py']


OPTIONS = {
'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS}, 
    setup_requires = ['py2app']
)