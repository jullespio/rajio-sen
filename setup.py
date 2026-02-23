from setuptools import find_packages
from setuptools import setup

from rajio_sen.app import App
import io

app = App()

DESCRIPTION = (
    "ラジオ船 (Rajio-Sen): A minimalist vaporwave-inspired pirate radio scanner for the terminal."
)
VERSION = app.get_version()


def readme():
    with io.open("README.md", "r", encoding="utf-8") as f:
        return f.read()


def required(sfx=""):
    with io.open(f"requirements{sfx}.txt", encoding="utf-8") as f:
        return f.read().splitlines()


setup(
    name="rajio-sen",  # The official package name
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="radios api internet-radio cli app vaporwave pirate-radio",
    author="ジュレス (juresu)", 
    author_email="YOUR_EMAIL@HERE", 
    url="https://github.com/jullespio/rajio-sen",
    license="MIT",
    entry_points={
        "console_scripts": [
            "rajio = rajio_sen.__main__:main",      # The primary command
            "rajio-sen = rajio_sen.__main__:main",  # Alternative name
            "radio = rajio_sen.__main__:main",      # Legacy compatibility
        ]
    },
    packages=find_packages(exclude=["test*"]),
    install_requires=required(),
    extras_require={"dev": required("-dev")},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",  # Reflecting the new 0.1.0 status
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    python_requires=">=3.6",
    project_urls={
        "Source": "https://github.com/jullespio/rajio-sen/",
        "Upstream": "https://api.radio-browser.info/",
    },
)