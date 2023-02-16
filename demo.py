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
