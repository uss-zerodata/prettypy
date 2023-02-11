from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

VERSION = '0.0.1'
DESCRIPTION = 'PrettyPy - Pretty terminal output for Python'
LONG_DESCRIPTION = 'PrettyPy is a Python library for pretty terminal output.'

# Setting up
setup(
    name="prettypy",
    version=VERSION,
    author="zerodata",
    author_email="<zerodata@amissum.de>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'print', 'terminal', 'output', 'pretty',
              'color', 'status', 'bar', 'progress', 'spinner', 'loading'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
