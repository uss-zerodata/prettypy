import unittest
from io import StringIO
from unittest.mock import patch

from prettypy.composer import Composer
from prettypy.layout import Layout

DEFAULT_LAYOUTS: dict = {
    "error": {
        "prefix": ["[", "red", "reset", "reset"],
        "text": ["X", "red", "reset", "reset"],
        "suffix": ["]", "red", "reset", "reset"],
    },
    "warning": {
        "prefix": ["[", "yellow", "reset", "reset"],
        "text": ["!", "yellow", "reset", "reset"],
        "suffix": ["]", "yellow", "reset", "reset"],
    },
    "success": {
        "prefix": ["[", "green", "reset", "reset"],
        "text": ["✓", "green", "reset", "reset"],
        "suffix": ["]", "green", "reset", "reset"],
    },
    "info": {
        "prefix": ["[", "blue", "reset", "reset"],
        "text": ["i", "blue", "reset", "reset"],
        "suffix": ["]", "blue", "reset", "reset"],
    },
    "debug": {
        "prefix": ["[", "magenta", "reset", "reset"],
        "text": ["D", "magenta", "reset", "reset"],
        "suffix": ["]", "magenta", "reset", "reset"],
    },
    "notice": {
        "prefix": ["[", "cyan", "reset", "reset"],
        "text": ["!", "cyan", "reset", "reset"],
        "suffix": ["]", "cyan", "reset", "reset"],
    },
    "log": {
        "prefix": ["[", "reset", "reset", "reset"],
        "text": [">", "reset", "reset", "reset"],
        "suffix": ["]", "reset", "reset", "reset"],
    },
    "question": {
        "prefix": ["[", "yellow", "reset", "reset"],
        "text": ["?", "yellow", "reset", "reset"],
        "suffix": ["]", "yellow", "reset", "reset"],
    },
    "positive": {
        "prefix": ["[", "green", "reset", "reset"],
        "text": ["+", "green", "reset", "reset"],
        "suffix": ["]", "green", "reset", "reset"],
    },
    "negative": {
        "prefix": ["[", "red", "reset", "reset"],
        "text": ["-", "red", "reset", "reset"],
        "suffix": ["]", "red", "reset", "reset"],
    },
    "neutral": {
        "prefix": ["[", "reset", "reset", "reset"],
        "text": [" ", "reset", "reset", "reset"],
        "suffix": ["]", "reset", "reset", "reset"],
    },
}


class TestComposer(unittest.TestCase):
    def test_default_layouts(self):
        composer = Composer()
        self.assertEqual(list(composer._layouts.keys()),
                         list(DEFAULT_LAYOUTS.keys()), "Missing layout keys")

    def test__init__(self):
        composer = Composer()
        self.assertEqual(composer._no_color,
                         False, "No color should be False")
        self.assertEqual(list(composer._layouts.keys()),
                         list(DEFAULT_LAYOUTS.keys()), "Default layouts are not loaded correctly")
        self.assertEqual(type(composer._layouts["error"]),
                         Layout, "Object type is not Layout")
        composer = Composer(no_color=True)
        self.assertEqual(composer._no_color,
                         True, "No color should be True")

    def test__iter__(self):
        composer = Composer()
        length = 0
        for layout in composer:
            length += 1
            self.assertEqual(type(layout),
                             Layout, "Object type is not Layout")
        self.assertEqual(length, len(composer._layouts),
                         "Not all layouts are iterated")

    def test__list__(self):
        composer = Composer()
        self.assertEqual(composer.__list__(),
                         list(composer._layouts.values()), "List is not correct")
        self.assertEqual(type(composer.__list__()[0]),
                         Layout, "Object type is not Layout")

    def test_add(self):
        composer = Composer()
        composer.add("test", "test")
        self.assertEqual(type(composer._layouts["test"]),
                         Layout, msg="Object type is not Layout")
        self.assertEqual(composer._layouts["test"].prefix,
                         ["", "reset", "reset", "reset"], "Prefix is not correct")
        self.assertEqual(composer._layouts["test"].text,
                         ["test", "reset", "reset", "reset"], "Text is not correct")
        self.assertEqual(composer._layouts["test"].suffix,
                         ["", "reset", "reset", "reset"], "Suffix is not correct")
        composer.add("test", "test", "blue", "red", "bold")
        self.assertEqual(composer._layouts["test"].text,
                         ["test", "blue", "red", "bold"], "Error when formatting text")

    def test_get(self):
        composer = Composer()
        self.assertEqual(type(composer.get("error")),
                         Layout, msg="Object type is not Layout")
        self.assertEqual(composer.get("error").prefix,
                         ["[", "red", "reset", "reset"], "Prefix is not correct")
        self.assertEqual(composer.get("error").text,
                         ["X", "red", "reset", "reset"], "Text is not correct")
        self.assertEqual(composer.get("error").suffix,
                         ["]", "red", "reset", "reset"], "Suffix is not correct")

    def test_list(self):
        composer = Composer()
        self.assertEqual(composer.list_modes(),
                         list(composer._layouts.keys()), "List is not correct")
        self.assertEqual(type(composer.list_modes()[0]),
                         str, "Object type is not str")

    def test_remove(self):
        composer = Composer()
        composer.remove("error")
        self.assertEqual("error" in composer._layouts,
                         False, "Layout is not removed")

    def test_compose(self):
        composer = Composer(no_color=True)
        self.assertEqual(composer.compose("error", "test"),
                         "[X] test", "Compose is not correct")
        composer = Composer()
        self.assertEqual(composer.compose("error", "test"),
                         "\x1b[31m[\x1b[0m\x1b[31mX\x1b[0m\x1b[31m]\x1b[0m test", "Compose is not correct")

    def test_print(self):
        composer = Composer(no_color=True)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            composer.print("error", "test")
            self.assertEqual(fake_out.getvalue(),
                             "[X] test\n", "Print is not correct")

    def test_set_padding(self):
        composer = Composer()
        composer.add("test", "test")
        composer.set_padding()
        self.assertEqual(composer.get("error").min_length,
                         4, "Padding is not correct")
        composer.set_padding(1)
        self.assertEqual(composer.get("error").min_length,
                         4, "Padding is not correct")
        composer.set_padding(10)
        self.assertEqual(composer.get("error").min_length,
                         10, "Padding is not correct")
