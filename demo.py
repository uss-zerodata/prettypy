from prettypy import Pretty

# This is a list of default modes currently supported by PrettyPy.
modes = ["info", "success", "warning", "error", "debug", "notice", "log", "question", "positive", "negative", "neutral"]

# To use PrettyPy, you must first create an instance of the Pretty class.
pretty = Pretty()

# You can then use the Pretty class to select a mode and print a message.
# The following code will print a message in each mode.
for mode in modes:
    pretty.__getattribute__(mode)(f"This is a {mode} message.")

# You can also reassign pythons built-in print function to one of PrettyPy's modes.
print = pretty.neutral
print("This is a neutral message printed using the print function.")

# To further customize the output, you can use the Composer class to create your own layouts.
composer = pretty.get_composer()

# Simply call the add method to create a new layout.
composer.add("important", "[IMPORTANT]", "yellow", text_format="bold")
composer.add("test", "[TEST]", "yellow", text_format="bold")

# After creating a new layout, you can use it like any other mode through the composer print method.
composer.print("important", "This is a test message printed using the composer print method.")
composer.print("test", "This is a test message printed using the composer print method.")

# The Composer also allows you to change the padding of the layout.
# This allows you to align all of your messages and improve the readability of your output.
composer.set_padding()

# To demonstrate the padding, we will print a message in each mode again.
for mode in modes:
    pretty.__getattribute__(mode)(f"This is a {mode} message.")
composer.print("important", "This is a test message printed using the composer print method.")
composer.print("test", "This is a test message printed using the composer print method.")
