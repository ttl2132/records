#!/usr/bin/env python

"""
Install records package. To install locally use:
    'pip install -e ."
"""

from setuptools import setup

setup(
    name="records",
    version="0.0.1",
    packages=[],
    install_requires=["pandas"],
    entry_points={
        "console_scripts": ["piglatin = piglatin.__main__:run_program"]
    }
)
