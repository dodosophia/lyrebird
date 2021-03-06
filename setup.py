import runpy
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

VERSION = runpy.run_path(
    os.path.join(here, "lyrebird", "version.py")
)["VERSION"]

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='lyrebird',
    version=VERSION,
    packages=['lyrebird'],
    url='https://github.com/meituan/lyrebird',
    author='HBQA',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    entry_points={
        'console_scripts': [
            'lyrebird = lyrebird.manager:main'
        ]
    },
    install_requires=[
        "beautifulsoup4==4.7.1",
        "colorama==0.4.1",
        "elasticsearch==7.0.1",
        "Flask==1.1.1",
        "Flask-RESTful==0.3.7",
        "Flask-SocketIO==4.2.1",
        "mitmproxy==4.0.4",
        "packaging==19.0",
        "portpicker==1.3.1",
        "requests==2.21.0",
        "SQLAlchemy==1.3.1",
        "click==6.7",
        "urllib3==1.24.1"
    ],
    extras_require={
        'dev': [
            "autopep8",
            "pylint",
            "pytest"
        ]
    }
)
