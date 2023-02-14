from shutil import get_terminal_size
from prettypy import style


layout_prefix: list = ["", "reset", "reset", "reset"]
layout_text: list = ["", "reset", "reset", "reset"]
layout_suffix: list = ["", "reset", "reset", "reset"]
min_length: int = 0


def __call__(text: str, fg: str = "reset", bg: str = "reset", fm: str = "reset") -> str:
    """
    Quick style layout_text.
    This is a shortcut for set_text, render.
    :param text: Text to style
    :param fg: Foreground color
    :param bg: Background color
    :param fm: Text format
    :return: Formatted text

    Example:
        layout.__call__("Hello World", "black", "yellow", "underline")
    """
    set_text(text, fg, bg, fm)
    return render()


def set_prefix(text: str, fg: str = "reset", bg: str = "reset", fm: str = "reset") -> None:
    """
    Set layout_prefix for layout_text.
    :param text: Text to style
    :param fg: Foreground color
    :param bg: Background color
    :param fm: Text format
    """
    layout_prefix[0] = text
    layout_prefix[1] = fg
    layout_prefix[2] = bg
    layout_prefix[3] = fm


def set_text(text: str, fg: str = "reset", bg: str = "reset", fm: str = "reset") -> None:
    """
    Set layout_text to style.
    :param text: Text to style
    :param fg: Foreground color
    :param bg: Background color
    :param fm: Text format
    """
    layout_text[0] = text
    layout_text[1] = fg
    layout_text[2] = bg
    layout_text[3] = fm


def set_suffix(text: str, fg: str = "reset", bg: str = "reset", fm: str = "reset") -> None:
    """
    Set layout_suffix for layout_text.
    :param text: Text to style
    :param fg: Foreground color
    :param bg: Background color
    :param fm: Text format
    """
    layout_suffix[0] = text
    layout_suffix[1] = fg
    layout_suffix[2] = bg
    layout_suffix[3] = fm


def set_min_length(length: int) -> None:
    """
    Set minimum length of the finished render.
    This is useful for padding.
    :param length: Minimum length
    """
    global min_length
    min_length = length


def render() -> str:
    """
    Render styled layout_text.
    :return: Styled layout_text
    """
    prefix = style.stylize(layout_prefix[0], layout_prefix[1], layout_prefix[2], layout_prefix[3])
    text = style.stylize(layout_text[0], layout_text[1], layout_text[2], layout_text[3])
    suffix = style.stylize(layout_suffix[0], layout_suffix[1], layout_suffix[2], layout_suffix[3])
    render = f"{prefix}{text}{suffix}"

    length = len(layout_prefix[0]) + len(layout_text[0]) + len(layout_suffix[0])
    if min_length > 0:
        if length < min_length:
            render += " " * (min_length - length)
    return render


if __name__ == '__main__':
    set_prefix("[", "yellow")
    set_text("'-'", "yellow", fm="bold")
    set_suffix("]", "yellow")
    print(render())
