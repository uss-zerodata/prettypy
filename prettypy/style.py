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


def stylize(text: str, fg: str = "reset", bg: str = "reset", st: str = "reset") -> str:
    """
    Style text with ANSI escape sequences.
    :param text: Text to style
    :param fg: Foreground color
    :param bg: Background color
    :param st: Style to apply
    :return: Formatted text

    Example:
    stylize("Hello World", "black", "yellow", "underline")
    stylize("Hello World", st="italic")
    """
    _fg = FOREGROUND[fg]
    _bg = BACKGROUND[bg]
    _style = FORMAT[st]
    return f"\033[{_style};{_fg};{_bg}m{text}\033[0m"


if __name__ == '__main__':
    print(stylize("Hello World", "black", "yellow", "underline"))
    print(stylize("Hello World", st="italic"))