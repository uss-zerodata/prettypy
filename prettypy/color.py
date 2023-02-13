class Color:
    def __init__(self):
        self. foreground: dict = {
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

        self.background: dict = {
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

        self.format: dict = {
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

    def colorize(self, text: str, _fg: str = None, _bg: str = None, _style: str = None) -> str:
        """
        Colorize text with ANSI escape sequences.
        :param text: Text to colorize
        :param _fg: Foreground color (optional)
        :param _bg: Background color (optional)
        :param _style: Style to apply (optional)
        :return: Formatted text

        Example:
        styles._colorize("Hello World", "red", "blue", "bold")
        """
        if _fg is None:
            _fg = "reset"
        if _bg is None:
            _bg = "reset"
        if _style is None:
            _style = "reset"

        if self.foreground[_fg]:
            _fg = self.foreground[_fg]
        else:
            _fg = self.foreground["reset"]
        if self.background[_bg]:
            _bg = self.background[_bg]
        else:
            _bg = self.background["reset"]
        if self.format[_style]:
            _style = self.format[_style]
        else:
            _style = self.format["reset"]

        return f"\033[{_style};{_fg};{_bg}m{text}\033[0m"
