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


def list_fg() -> list:
    """
    List all foreground fg_color names.
    :return: List of foreground colors
    """
    return list(FOREGROUND.keys())


def list_bg() -> list:
    """
    List all background fg_color names.
    :return: List of background colors
    """
    return list(BACKGROUND.keys())


def list_fm() -> list:
    """
    List all text text_format names.
    :return: List of formats
    """
    return list(FORMAT.keys())


def stylize(text: str, fg: str = "reset", bg: str = "reset", fm: str = "reset", _no_color: bool = False) -> str:
    """
    Style text with ANSI escape sequences.
    :param text: Text to text_format
    :param fg: Foreground fg_color
    :param bg: Background fg_color
    :param fm: Text text_format
    :param _no_color: Disable color
    :return: Formatted text

    Example:
        stylize("Hello World", "black", "yellow", "underline")
    """
    if fg == "reset" and bg == "reset" and fm == "reset":
        return text
    if _no_color:
        return text
    _fg: str = FOREGROUND[fg]
    _bg: str = BACKGROUND[bg]
    _fm: str = FORMAT[fm]

    separate: bool = False
    ansi_code: str = "\033["

    if fg != "reset":
        ansi_code += f"{_fg}"
        separate = True
    if bg != "reset":
        if separate:
            ansi_code += ";"
            separate = False
        ansi_code += f"{_bg}"
        separate = True
    if fm != "reset":
        if separate:
            ansi_code += ";"
        ansi_code += f"{_fm}"

    return f"{ansi_code}m{text}\033[0m"
