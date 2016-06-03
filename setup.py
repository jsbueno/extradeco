from setuptools import setup

setup(
    name = 'extradeco',
    py_modules = ["extradeco"],
    version = "0.1.1",
    license = "LGPLv3+",
    author = "João S. O. Bueno",
    author_email = "gwidion@gmail.com",
    description = "Decorator utils. Currently 'paremetrized': a decorator to enable flat decorators: call the wrapped func straight from your decorator body",
    keywords = "decorator utils simplifier",
    url = 'https://github.com/jsbueno/extradeco',
    long_description = open('README.md').read(),
    test_requites = ["pytest"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ]
)
