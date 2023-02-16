# PrettyPy
    
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/prettypy)
[![PyPI version](https://badge.fury.io/py/prettypy.svg)](https://badge.fury.io/py/prettypy)
![PyPI - Downloads](https://img.shields.io/pypi/dm/prettypy)

PrettyPy is a Python library that simplifies printing colored and styled messages in CLI applications. With PrettyPy, you can easily print status updates, error messages, and other types of messages with colored indicators that help them stand out.

The library offers a straightforward API for creating custom layouts, as well as a range of pre-built layouts that you can use to enhance the readability of your CLI applications.

PrettyPy uses ANSI escape codes to provide its coloring functionality, which is supported by most terminals. If your terminal does not support ANSI escape codes, you can set the no-color flag to disable the coloring functionality.

By using PrettyPy, you can create user-friendly CLI applications that are easier to read and more engaging.

- [GitHub](https://github.com/uss-zerodata/prettypy)
- [PyPi](https://pypi.org/project/prettypy)

## Features

- [x] Print messages with colors and styles
- [x] Create custom layouts
- [x] No color mode
- [ ] Table output
- [ ] Updating messages
- [ ] Progress bars
- [ ] Spinners
- [ ] Desktop notifications

## Installation

```bash
pip install prettypy
```

## Usage

~~~python
from prettypy import Pretty

# Create a new Pretty object
p = Pretty()

# Print an error message
p.error('Something went wrong')

# Print a success message
p.success('Everything is fine')

# Customize the output with composer
c = p.get_composer()

# Add a simple layout
c.add('simple', '[S]', 'blue')

# Print a message with the simple layout
c.compose('simple', 'This is a simple message')
~~~

> <span style="color: red">[✗]</span> Something went wrong <br>
> <span style="color: green">[✓]</span> Everything is fine <br>
> <span style="color: blue">[S]</span> This is a simple messages

---

![GitHub repo size](https://img.shields.io/github/repo-size/uss-zerodata/prettypy)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/uss-zerodata/prettypy)

![GitHub issues](https://img.shields.io/github/issues/uss-zerodata/prettypy)
![GitHub closed issues](https://img.shields.io/github/issues-closed/uss-zerodata/prettypy)
![GitHub pull requests](https://img.shields.io/github/issues-pr/uss-zerodata/prettypy)

![GitHub contributors](https://img.shields.io/github/contributors/uss-zerodata/prettypy)
