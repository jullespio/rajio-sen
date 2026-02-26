import io
import os
import re
from setuptools import find_packages, setup

def get_metadata():
    """Extract metadata from __about__.py safely."""
    metadata = {}
    base_path = os.path.abspath(os.path.dirname(__file__))
    about_path = os.path.join(base_path, "rajio_sen", "__about__.py")
    
    # Shield 1: Check if file exists in the isolated build directory
    if os.path.exists(about_path):
        with io.open(about_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Flexible regex to capture variables regardless of spacing
            matches = re.findall(r"^__(.*)__\s*=\s*['\"]([^'\"]*)['\"]", content, re.M)
            for key, value in matches:
                metadata[key.lower()] = value
                
    # Shield 2: Map fallbacks to prevent KeyErrors
    if 'url' not in metadata and 'website' in metadata:
        metadata['url'] = metadata['website']
        
    return metadata

info = get_metadata()

DESCRIPTION = (
    "ラジオ船 (Rajio-Sen): A minimalist vaporwave-inspired pirate radio scanner for the terminal."
)

def readme():
    # Shield 3: Fallback if README.md is not copied to the temp build env
    try:
        with io.open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return DESCRIPTION

def required(sfx=""):
    # Shield 4: Fallback if requirements.txt is missing during discovery
    try:
        with io.open(f"requirements{sfx}.txt", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return ["requests", "rich"]

setup(
    name="rajio-sen",
    # Shield 5: Use .get() with default fail-safes so it never crashes
    version=info.get("version", "1.2.0"),
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="radios api internet-radio cli app vaporwave pirate-radio",
    author=info.get("author", "ジュレス (juresu)"), 
    author_email=info.get("email", "jullespio@users.noreply.github.com"), 
    url=info.get("url", "https://github.com/jullespio/rajio-sen"),
    license="MIT",
    entry_points={
        "console_scripts": [
            "rajio = rajio_sen.__main__:main",
            "rajio-sen = rajio_sen.__main__:main",
        ]
    },
    packages=find_packages(exclude=["test*"]),
    install_requires=required(),
    extras_require={"dev": required("-dev")},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",        
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    python_requires=">=3.6",
    project_urls={
        "Source": info.get("url", "https://github.com/jullespio/rajio-sen"),
        "Upstream": "https://api.radio-browser.info/",
    },
)