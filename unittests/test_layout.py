import unittest

from prettypy.layout import Layout


class TestLayout(unittest.TestCase):
    def test__init__(self):
        layout = Layout()
        self.assertEqual(layout._no_color, False)
        self.assertEqual(layout.name, "default")
        self.assertEqual(layout.prefix, ["", "reset", "reset", "reset"])
        self.assertEqual(layout.text, ["", "reset", "reset", "reset"])
        self.assertEqual(layout.suffix, ["", "reset", "reset", "reset"])
        self.assertEqual(layout.min_length, 0)
        layout = Layout("text", True)
        self.assertEqual(layout._no_color, True)
        self.assertEqual(layout.name, "text")

    def test__call__(self):
        layout = Layout()
        self.assertEqual(layout.__call__("Hello World"),
                         "Hello World", "Minimal text is not rendered correctly.")
        self.assertEqual(layout.__call__("Hello World", "black", "yellow", "underline"),
                         "\033[30;43;4mHello World\033[0m", "Error when adding text_format.")
        self.assertEqual(layout.__call__("Hello World", "black", "yellow", "underline", "text"),
                         "\033[30;43;4mHello World\033[0m text", "Error when adding message.")
        self.assertEqual(layout.__call__(text="Hello World", fg="black", bg="yellow", fm="underline", msg="text"),
                         "\033[30;43;4mHello World\033[0m text", "Naming convention is not respected.")

    def test__str__(self):
        layout = Layout()
        self.assertEqual(layout.__str__(),
                         "default", "Default name is not 'default'.")
        layout = Layout("text")
        self.assertEqual(layout.__str__(),
                         "text", "Name not set correctly.")

    def test__len__(self):
        layout = Layout()
        self.assertEqual(len(layout),
                         0, "Empty layout")
        layout.set_prefix("text")
        self.assertEqual(len(layout),
                         4, "Errpr when adding prefix.")
        layout.set_text("text")
        self.assertEqual(len(layout),
                         8, "Error when adding text.")
        layout.set_suffix("text")
        self.assertEqual(len(layout),
                         12, "Error when adding suffix.")

    def test_set_prefix(self):
        layout = Layout()
        layout.set_prefix("text")
        self.assertEqual(layout.prefix,
                         ["text", "reset", "reset", "reset"], "Error when setting prefix.")
        layout.set_prefix("text", "black", "yellow", "underline")
        self.assertEqual(layout.prefix,
                         ["text", "black", "yellow", "underline"], "Error when adding text_format.")

    def test_set_text(self):
        layout = Layout()
        layout.set_text("text")
        self.assertEqual(layout.text,
                         ["text", "reset", "reset", "reset"], "Error when setting text.")
        layout.set_text("text", "black", "yellow", "underline")
        self.assertEqual(layout.text,
                         ["text", "black", "yellow", "underline"], "Error when adding text_format.")

    def test_set_suffix(self):
        layout = Layout()
        layout.set_suffix("text")
        self.assertEqual(layout.suffix,
                         ["text", "reset", "reset", "reset"], "Error when setting suffix.")
        layout.set_suffix("text", "black", "yellow", "underline")
        self.assertEqual(layout.suffix,
                         ["text", "black", "yellow", "underline"], "Error when adding text_format.")

    def test_set_padding(self):
        layout = Layout()
        layout.set_padding(10)
        self.assertEqual(layout.min_length, 10, "Error when setting padding.")

    def test_render(self):
        layout = Layout()
        self.assertEqual(layout.render(),
                         "", "Error when rendering empty layout.")
        layout.set_prefix("[")
        layout.set_padding(10)
        self.assertEqual(layout.render(),
                         "[         ", "Error when rendering layout with padding.")
        layout.set_padding(0)
        self.assertEqual(layout.render(),
                         "[", "Error when removing padding.")
        self.assertEqual(layout.render(),
                         "[", "Error when rendering layout with prefix.")
        layout.set_text("text")
        self.assertEqual(layout.render(),
                         "[text", "Error when rendering layout with text.")
        layout.set_suffix("]")
        self.assertEqual(layout.render(),
                         "[text]", "Error when rendering layout with suffix.")
        layout.set_prefix("[", "black", "yellow", "underline")
        self.assertEqual(layout.render(),
                         "\033[30;43;4m[\033[0mtext]", "Error when rendering layout with stylized prefix.")
        self.assertEqual(layout.render("text"),
                         "\033[30;43;4m[\033[0mtext] text", "Error when rendering with message.")
