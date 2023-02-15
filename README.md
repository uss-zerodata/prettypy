# prettypy

Easily format terminal output with colors and styles.

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
~~~
> <span style="color: red">[✗]</span> Something went wrong <br>
> <span style="color: green">[✓]</span> Everything is fine

~~~python
# Customize the output with composer
c = p.get_composer()

# Add a simple layout
c.add('simple', '[S]', 'blue')

# Print a message with the simple layout
c.compose('simple', 'This is a simple message')
~~~
> <span style="color: blue">[S]</span> This is a simple messages

## Documentation


