from setuptools import setup, find_packages
import codecs
import os

from lazerpay import __version__

here = os.path.abspath(os.path.dirname(__file__))

VERSION = __version__
DESCRIPTION = 'Lazerpay Python SDK'

# Setting up
setup(
    name="lazerpay-sdk",
    version=VERSION,
    author="Kenneth Gabriel",
    author_email="kennethgabriel78@gmail.com",
    description=DESCRIPTION,
    long_description="""
    **Github Repo**:  [https://github.com/keosariel/lazerpay-py-sdk](https://github.com/keosariel/lazerpay-py-sdk)
    **Documentation**: [https://github.com/keosariel/lazerpay-py-sdk/blob/master/README.md](https://github.com/keosariel/lazerpay-py-sdk/blob/master/README.md)
    """,
    long_description_content_type="text/markdown",
    url="https://github.com/keosariel/lazerpay-py-sdk",
    packages=find_packages(),
    license="MIT",
    install_requires=[
        "aiohttp >= 3.7.4",
    ],
    extras_require={
        "dotenv": ["python-dotenv"],
    },
    keywords=['python', 'lazerpay', 'request', 'aiohttp', 'client'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)