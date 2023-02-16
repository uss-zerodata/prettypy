# PrettyPy
    
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/prettypy)
[![PyPI version](https://badge.fury.io/py/prettypy.svg)](https://badge.fury.io/py/prettypy)
![PyPI - Downloads](https://img.shields.io/pypi/dm/prettypy)

PrettyPy is a Python library. It provides a simple API for printing messages with colours and styles.
Colour output is a great way to make your CLI applications more user-friendly and readable.
Status messages, error messages and other types of messages can be printed with coloured indicators to make them stand out from the rest.

To create custom layouts and print messages with them, PrettyPy provides a simple API.
To quickly improve the readability of your CLI applications, it also provides a set of default layouts.

ANSI escape codes are used for colouring. These are supported by most devices.

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
