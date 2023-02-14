from prettypy import style


class Layout:
    def __init__(self, name: str = "default") -> None:
        """
        Initialize layout.
        """
        self.name: str = name
        self.prefix: list = ["", "reset", "reset", "reset"]
        self.test: list = ["", "reset", "reset", "reset"]
        self.suffix: list = ["", "reset", "reset", "reset"]
        self._min_length: int = 0

    def __call__(self, text: str, fg: str = "reset", bg: str = "reset",
                 fm: str = "reset", msg: str = None) -> str:
        """
        Quick style test.
        This is a shortcut for set_text, render.
        :param text: Text to style
        :param fg: Foreground color
        :param bg: Background color
        :param fm: Text format
        :return: Formatted text

        Example:
            layout.__call__("Hello World", "black", "yellow", "underline")
        """
        self.set_text(text, fg, bg, fm)
        return self.render(msg)

    def __str__(self) -> str:
        """
        Return name.
        """
        return self.name

    def set_prefix(self, text: str, fg: str = "reset", bg: str = "reset",
                   fm: str = "reset") -> None:
        """
        Set prefix for test.
        :param text: Text to style
        :param fg: Foreground color
        :param bg: Background color
        :param fm: Text format
        """
        self.prefix[0] = text
        self.prefix[1] = fg
        self.prefix[2] = bg
        self.prefix[3] = fm

    def set_text(self, text: str, fg: str = "reset", bg: str = "reset",
                 fm: str = "reset") -> None:
        """
        Set test to style.
        :param text: Text to style
        :param fg: Foreground color
        :param bg: Background color
        :param fm: Text format
        """
        self.test[0] = text
        self.test[1] = fg
        self.test[2] = bg
        self.test[3] = fm

    def set_suffix(self, text: str, fg: str = "reset", bg: str = "reset",
                   fm: str = "reset") -> None:
        """
        Set suffix for test.
        :param text: Text to style
        :param fg: Foreground color
        :param bg: Background color
        :param fm: Text format
        """
        self.suffix[0] = text
        self.suffix[1] = fg
        self.suffix[2] = bg
        self.suffix[3] = fm

    def set_padding(self, length: int) -> None:
        """
        Set minimum length of the finished render.
        This is useful for padding.
        :param length: Minimum length
        """
        self._min_length = length

    def get_effective_length(self) -> int:
        """
        Get effective length of the finished render.
        :return: Effective length
        """
        length = len(self.prefix[0]) + len(self.test[0]) + len(self.suffix[0])
        return length

    def render(self, msg: str = None) -> str:
        """
        Render styled test.
        :return: Styled test
        """
        prefix = style.stylize(self.prefix[0], self.prefix[1], self.prefix[2],
                               self.prefix[3])
        text = style.stylize(self.test[0], self.test[1], self.test[2],
                             self.test[3])
        suffix = style.stylize(self.suffix[0], self.suffix[1], self.suffix[2],
                               self.suffix[3])
        render = f"{prefix}{text}{suffix}"

        if self._min_length > 0:
            if self.get_effective_length() < self._min_length:
                render += " " * (self._min_length
                                 - self.get_effective_length())

        if msg is not None:
            render += f" {msg}"
        return render


if __name__ == '__main__':
    layout = Layout("test")
    layout.set_prefix("[", "yellow")
    layout.set_text("'-'", "yellow", fm="bold")
    layout.set_suffix("]", "yellow")
    print(layout.render("hello world"))
