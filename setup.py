from setuptools import find_packages, setup
from distutils.core import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="tornado-async-transformer",
    version="0.3.0",
    description="libcst transformer and codemod for updating tornado @gen.coroutine syntax to python3.5+ native async/await",
    url="https://github.com/jgibo/tornado-async-transformer",
    packages=find_packages(),
    install_requires=["libcst == 1.0.1"],
    author="Zach Hammer, Jordan Gibbings",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.11",
    ],
)
