from setuptools import setup, find_packages

setup(
    name="LibScan",
    version="1.0.0",
    author="AKM Korishee Apurbo",
    author_email="bandinvisible8@gmail.com",
    description="LibScan: A Python dependency scanner and installer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/IMApurbo/LibScan",  # Update with your repo
    packages=find_packages(),
    install_requires=[
        "rich",
        "click",
    ],
    entry_points={
        "console_scripts": [
            "libscan=libscan.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
