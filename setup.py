#!/usr/bin/env python
from setuptools import setup

setup(
    name="kuroneko",
    version="0.1.0",
    description="Kuroneko CLI",
    author="Gustavo Bezerra",
    author_email="gusutabopb@gmail.com",
    url="https://github.com/gusutabopb/kuroneko",
    packages=["kuroneko"],
    license="MIT",
    install_requires=["requests", "terminaltables", "beautifulsoup4"],
    entry_points={"console_scripts": ["kuroneko=kuroneko.kuroneko:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
