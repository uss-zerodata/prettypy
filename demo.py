from prettypy import Pretty

# To use PrettyPy, you must first create an instance of the Pretty class.
pretty = Pretty()

# The Pretty class has a method for each mode.
# Each method takes a message as its only argument.
pretty.info("This is an info message.")
pretty.success("This is a success message.")

# You can also use the Pretty class as a dictionary.
for mode in pretty:
    pretty.__getattribute__(mode.name)(f"This is a {mode} message.")

# You can also reassign pythons built-in print function to one of PrettyPy's modes.
print = pretty.neutral
print("This is a neutral message printed using the print function.")

# To further customize the output, you can use the Composer class to create your own layouts.
composer = pretty.get_composer()

# Simply call the add method to create a new layout.
pretty.add("test", "[TEST]", "red", text_format="bold")

# After creating a new layout, you can use it like any other mode through the composer print method.
pretty.test("This is a test message printed using the composer print method.")

# The Composer also allows you to change the padding of the layout.
# This allows you to align all of your messages and improve the readability of your output.
composer.set_padding()

# To demonstrate the padding, we will print a few messages again.
pretty.info("This is an info message.")
pretty.success("This is a success message.")
pretty.test("This is a test message printed using the composer print method.")
