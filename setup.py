"""Setup for Code Katas."""

from setuptools import setup

setup(
    name='code katas',
    description='Completed Code Wars katas, with tests.',
    author='Chelsea Dole',
    author_email='chelseadole@gmail',
    package_dir={' ': 'src'},
    py_modules=['ackermann'],
    install_requires=['ipython', 'express'],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']}
)
