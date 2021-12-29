from textwrap import dedent as D

from setuptools import setup

setup(
    name = 'extradeco',
    py_modules = ["extradeco"],
    version = "0.1.2",
    license = "LGPLv3+",
    author = "João S. O. Bueno",
    author_email = "gwidion@gmail.com",
    description = D("""\
        Decorator utilities
        ====================

        Currently, just "parametrized" is included. 


        paremetrized
        ------------

        a decorator to enable flat decorators: 
        Write your decorator with the function to be decorated as first parameter,
        and it straight from your decorator body:

        ```
        @extradeco.parametrized
        def logger(func, *args, **kw):
            nonlocal f_args
            f_args = args
            return func(*args, **kw)

        @logger()
        def s(a,b):
            return a + b
        ```
        """),
    keywords = "decorator utils simplifier",
    url = 'https://github.com/jsbueno/extradeco',
    long_description = open('README.md').read(),
    test_requites = ["pytest"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ]
)
