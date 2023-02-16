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

## Getting Started

The PrettyPy package is a Python library that provides an easy-to-use API for printing colored and styled messages in CLI applications. With the help of PrettyPy, you can quickly and easily print status updates, error messages, and other types of messages with colored indicators that help them stand out and improve the readability of your CLI applications.

To start using PrettyPy, you need to create an instance of the Pretty class. Once you have done this, you can use the Pretty class methods for each mode to print your messages. You can also use the Pretty class as a dictionary to access its modes, and you can even reassign Python's built-in print function to one of PrettyPy's modes.

If you need to create your own layouts, you can use the Composer class to customize the output even further. The Composer allows you to add new layouts, change the padding of the layout to align all your messages and improve the readability of your output.

Here's a code example that demonstrates how to use the PrettyPy package:

~~~python
from prettypy import Pretty

# Create an instance of the Pretty class
pretty = Pretty()

# Use the Pretty class methods for each mode to print messages
pretty.info("This is an info message.")
pretty.success("This is a success message.")

# Access Pretty class modes as a dictionary
for mode in pretty:
    pretty.__getattribute__(mode.name)(f"This is a {mode} message.")

# Reassign Python's built-in print function to one of PrettyPy's modes
print = pretty.neutral
print("This is a neutral message printed using the print function.")

# Use the Composer class to create new layouts
composer = pretty.get_composer()
pretty.add("test", "[TEST]", "red", text_format="bold")

# Use new layout created by the composer print method
pretty.test("This is a test message printed using the composer print method.")

# Change the padding of the layout with the Composer
composer.set_padding()

# Print messages again to demonstrate the padding
pretty.info("This is an info message.")
pretty.success("This is a success message.")
pretty.test("This is a test message printed using the composer print method.")
~~~

> <span style="color: blue">[i]</span> This is an info message. <br>
> <span style="color: green">[✓]</span> This is a success message. <br>
> <span style="color: red">[X]</span> This is a error message. <br>
> ...

With the PrettyPy package, you can make your CLI applications more user-friendly, readable, and engaging. The package is easy to use, and it allows you to quickly and easily create custom layouts to suit your needs.

---

![GitHub repo size](https://img.shields.io/github/repo-size/uss-zerodata/prettypy)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/uss-zerodata/prettypy)

![GitHub issues](https://img.shields.io/github/issues/uss-zerodata/prettypy)
![GitHub closed issues](https://img.shields.io/github/issues-closed/uss-zerodata/prettypy)
![GitHub pull requests](https://img.shields.io/github/issues-pr/uss-zerodata/prettypy)

![GitHub contributors](https://img.shields.io/github/contributors/uss-zerodata/prettypy)
