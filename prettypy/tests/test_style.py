import unittest
import prettypy.style as style


class TestStyle(unittest.TestCase):
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
                         "\033[4;30;43mHello World\033[0m", "Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", "black", "yellow", "reset"),
                         "\033[0;30;43mHello World\033[0m", "Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", "black", "reset", "underline"),
                         "\033[4;30;49mHello World\033[0m", "Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", "reset", "yellow", "underline"),
                         "\033[4;39;43mHello World\033[0m", "Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", "reset", "reset", "underline"),
                         "\033[4;39;49mHello World\033[0m", "Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", "black", "reset", "reset"),
                         "\033[0;30;49mHello World\033[0m", "Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", "reset", "yellow", "reset"),
                         "\033[0;39;43mHello World\033[0m", "Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", "reset", "reset", "reset"),
                         "\033[0;39;49mHello World\033[0m", "Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", "black", "yellow", "reset"),
                         "\033[0;30;43mHello World\033[0m", "Stylize does not match expected output.")
        self.assertEqual(style.stylize("Hello World", bg="red"),
                         "\033[0;39;41mHello World\033[0m", "Stylize does not match expected output.")


if __name__ == '__main__':
    unittest.main()
