import unittest
from prettypy import style

FOREGROUND: dict = {
    "black": "30",
    "red": "31",
    "green": "32",
    "yellow": "33",
    "blue": "34",
    "magenta": "35",
    "cyan": "36",
    "white": "37",
    "reset": "39",
    "bright_black": "90",
    "bright_red": "91",
    "bright_green": "92",
    "bright_yellow": "93",
    "bright_blue": "94",
    "bright_magenta": "95",
    "bright_cyan": "96",
    "bright_white": "97"
}

BACKGROUND: dict = {
    "black": "40",
    "red": "41",
    "green": "42",
    "yellow": "43",
    "blue": "44",
    "magenta": "45",
    "cyan": "46",
    "white": "47",
    "reset": "49",
    "bright_black": "100",
    "bright_red": "101",
    "bright_green": "102",
    "bright_yellow": "103",
    "bright_blue": "104",
    "bright_magenta": "105",
    "bright_cyan": "106",
    "bright_white": "107"
}

FORMAT: dict = {
    "reset": "0",
    "bold": "1",
    "dim": "2",
    "italic": "3",
    "underline": "4",
    "blink": "5",
    "reverse": "7",
    "hidden": "8",
    "strikethrough": "9"
}


class TestStyle(unittest.TestCase):
    def test_defaults(self):
        for element in FOREGROUND:
            self.assertEqual(style.FOREGROUND[element], FOREGROUND[element], "Default foreground colors incomplete.")
        for element in BACKGROUND:
            self.assertEqual(style.BACKGROUND[element], BACKGROUND[element], "Default background colors incomplete.")
        for element in FORMAT:
            self.assertEqual(style.FORMAT[element], FORMAT[element], "Default format colors incomplete.")

    def test_list_fg(self):
        fg_colors: int = 17
        self.assertGreaterEqual(len(style.list_fg()), fg_colors, "Default foreground colors incomplete.")
        sample: list = list(style.FOREGROUND.keys())
        self.assertEqual(style.list_fg(), sample, "Foreground fg_color list does not match default dictionary.")

    def test_list_bg(self):
        bg_colors: int = 17
        self.assertGreaterEqual(len(style.list_bg()), bg_colors, "Default background colors incomplete.")
        sample: list = list(style.BACKGROUND.keys())
        self.assertEqual(style.list_bg(), sample, "Background fg_color list does not match default dictionary.")

    def test_list_fm(self):
        fm_colors: int = 9
        self.assertGreaterEqual(len(style.list_fm()), fm_colors, "Default format colors incomplete.")
        sample: list = list(style.FORMAT.keys())
        self.assertEqual(style.list_fm(), sample, "Format fg_color list does not match default dictionary.")

    def test_stylize(self):
        self.assertEqual(style.stylize("Hello World", "black", "yellow", "underline"),
                         "\x1b[4;30;43mHello World\x1b[0m", "[1] Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", "reset", "reset", "reset"),
                         "\x1b[0;39;49mHello World\x1b[0m", "[2] Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", fg="bright_red", bg="bright_yellow", fm="bold"),
                         "\x1b[1;91;103mHello World\x1b[0m", "[3] Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", bg="bright_yellow"),
                         "\x1b[0;39;103mHello World\x1b[0m", "[4] Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", "black", "yellow", "strikethrough", _no_color=True),
                         "Hello World", "No color flag not working.")


if __name__ == '__main__':
    unittest.main()
