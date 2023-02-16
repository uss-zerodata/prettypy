from prettypy import style


class Layout:
    def __init__(self, name: str = "default", no_color: bool = False) -> None:
        """
        Initialize layout.
        """
        self._no_color: bool = no_color
        self.name: str = name
        self.prefix: list = ["", "reset", "reset", "reset"]
        self.test: list = ["", "reset", "reset", "reset"]
        self.suffix: list = ["", "reset", "reset", "reset"]
        self.min_length: int = 0

    def __call__(self, text: str, fg: str = "reset", bg: str = "reset", fm: str = "reset", msg: str = None) -> str:
        """
        Quick style test.
        This is a shortcut for set_text, render.
        :param text: Text to style
        :param fg: Foreground fg_color
        :param bg: Background fg_color
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

    def __len__(self):
        """
        Get effective length of the finished render.
        :return: Effective length
        """
        return len(self.prefix[0]) + len(self.test[0]) + len(self.suffix[0])

    def set_prefix(self, text: str, fg: str = "reset", bg: str = "reset", fm: str = "reset") -> None:
        """
        Set prefix for test.
        :param text: Text to style
        :param fg: Foreground fg_color
        :param bg: Background fg_color
        :param fm: Text format
        """
        self.prefix[0]: str = text
        self.prefix[1]: str = fg
        self.prefix[2]: str = bg
        self.prefix[3]: str = fm

    def set_text(self, text: str, fg: str = "reset", bg: str = "reset", fm: str = "reset") -> None:
        """
        Set test to style.
        :param text: Text to style
        :param fg: Foreground fg_color
        :param bg: Background fg_color
        :param fm: Text format
        """
        self.test[0]: str = text
        self.test[1]: str = fg
        self.test[2]: str = bg
        self.test[3]: str = fm

    def set_suffix(self, text: str, fg: str = "reset", bg: str = "reset", fm: str = "reset") -> None:
        """
        Set suffix for test.
        :param text: Text to style
        :param fg: Foreground fg_color
        :param bg: Background fg_color
        :param fm: Text format
        """
        self.suffix[0]: str = text
        self.suffix[1]: str = fg
        self.suffix[2]: str = bg
        self.suffix[3]: str = fm

    def set_padding(self, length: int) -> None:
        """
        Set minimum length of the finished render.
        This is useful for padding.
        :param length: Minimum length
        """
        self.min_length: int = length

    def render(self, msg: str = None) -> str:
        """
        Render styled test.
        :return: Styled test
        """
        prefix: str = style.stylize(self.prefix[0], self.prefix[1], self.prefix[2], self.prefix[3], self._no_color)
        text: str = style.stylize(self.test[0], self.test[1], self.test[2], self.test[3], self._no_color)
        suffix: str = style.stylize(self.suffix[0], self.suffix[1], self.suffix[2], self.suffix[3], self._no_color)
        render: str = f"{prefix}{text}{suffix}"

        if self.min_length > 0:
            if len(self) < self.min_length:
                render += " " * (self.min_length - len(self))

        if msg is not None:
            render += f" {msg}"
        return render


if __name__ == '__main__':
    layout: Layout = Layout("test")
    layout.set_prefix("[", "yellow")
    layout.set_text("'-'", "yellow", fm="bold")
    layout.set_suffix("]", "yellow")
    print(layout.render("hello world"))
