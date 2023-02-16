from prettypy.pretty_template import PrettyTemplate
from prettypy.composer import Composer


class Pretty(PrettyTemplate):
    def __init__(self, no_color: bool = False) -> None:
        """
        Initialize Pretty.
        """
        self._composer: Composer = Composer(no_color)
        self.update()

    def __call__(self, msg: str = "") -> str:
        """
        Quick display message.
        :param msg: Message to display
        :return: Formatted text
        """
        return self.neutral(msg)

    def __iter__(self):
        """
        Iterate over layouts.
        """
        for layout in self._composer:
            yield layout

    def __getattr__(self, item):
        """
        Get attribute.
        """
        pass

    def get_composer(self) -> Composer:
        """
        Get composer instance.
        :return: Composer
        """
        return self._composer

    def _make_method(self, name) -> callable:
        """
        Register a print function for each mode in the composer.
        """
        def _method(msg: str = "") -> str:
            """
            Display message.
            :param msg: Message to display
            :return: Formatted text
            """
            pretty: str = self._composer.compose(name, msg)
            print(pretty)
            return pretty
        return _method

    def update(self) -> None:
        """
        Update Pretty.
        """
        for layout in self._composer:
            setattr(self, layout.name, self._make_method(layout.name))

    def add(self, name: str, text: str, fg_color: str = "reset", bg_color: str = "reset",
            text_format: str = "reset") -> None:
        """
        Add a simple layout to the composer.
        :param name: Name of the layout
        :param text: Text to display
        :param fg_color: Foreground color
        :param bg_color: Background color
        :param text_format: Text format
        """
        self._composer.add(name, text, fg_color, bg_color, text_format)
        self.update()

    def remove(self, name: str) -> None:
        """
        Remove a layout from the composer.
        :param name: Name of the layout
        """
        self._composer.remove(name)
        self.update()
