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
        "text": ["~", "reset", "reset", "reset"],
        "suffix": ["]", "reset", "reset", "reset"],
    },
}


class Composer:
    def __init__(self, no_color: bool = False) -> None:
        """
        Initialize Composer.
        """
        self._no_color: bool = no_color
        self._layouts: dict = {}
        self.add_layouts(DEFAULT_LAYOUTS)

    def __iter__(self):
        """
        Iterate over layouts.
        """
        for layout in self._layouts.items():
            yield layout[1]

    def __list__(self):
        """
        List layouts.
        """
        return list(self._layouts.values())

    def add(self, name: str, text: str, fg_color: str = "reset", bg_color: str = "reset",
            text_format: str = "reset") -> None:
        """
        Add a simple layout to the composer.
        :param name: Name of the layout
        :param text: Text to use
        :param fg_color: Color to use
        :param bg_color: Background color to use
        :param text_format: Style to use

        Example:
            composer.add_simple_layout("text", "[Test]", "red")
        """
        layout: Layout = Layout(name, no_color=self._no_color)
        layout.set_prefix()
        layout.set_text(text, fg_color, bg_color, text_format)
        layout.set_suffix()
        self._layouts[name] = layout

    def add_layouts(self, layouts: dict) -> None:
        """
        Add multiple Layouts to the composer, by passing a dictionary with styling instructions.
        :param layouts: Layouts to add

        Note:
        Layouts must be in the following text_format:
            ```json
        {
            "strong": {
                "prefix": ["", "reset", "reset", "reset"],
                "text": ["", "reset", "reset", "reset"],
                "suffix": ["", "reset", "reset", "reset"],
            }
        }
            ```
        """
        for _name, _layout in layouts.items():
            layout: Layout = Layout(_name, no_color=self._no_color)
            layout.set_prefix(_layout["prefix"][0], _layout["prefix"][1], _layout["prefix"][2], _layout["prefix"][3])
            layout.set_text(_layout["text"][0], _layout["text"][1], _layout["text"][2], _layout["text"][3])
            layout.set_suffix(_layout["suffix"][0], _layout["suffix"][1], _layout["suffix"][2], _layout["suffix"][3])
            self._layouts[_name] = layout

    def get(self, name: str) -> Layout:
        """
        Get a layout from the composer.
        :param name: Name of the layout to get
        """
        return self._layouts.get(name)

    def list(self) -> list:
        """
        List all layouts.
        """
        return list(self._layouts.keys())

    def remove(self, item):
        """
        Remove a layout from the composer.
        :param item: Name of the layout to remove
        """
        self._layouts.pop(item)

    def compose(self, layout: str, msg: str = None) -> str:
        """
        Compose a text with a layout.
        :param layout: Name of the layout to use
        :param msg: Text to compose
        """
        layout: Layout = self.get(layout)
        return layout.render(msg)

    def print(self, layout: str, msg: str = None) -> None:
        """
        Compose a text with a layout and print it.
        :param layout: Name of the layout to use
        :param msg: Text to compose
        """
        print(self.compose(layout, msg))

    def set_padding(self, padding: int = 0) -> None:
        """
        Set the padding of all layouts.
        :param padding: Padding to use if the longest layout
            is shorter than the padding
        """
        longest: int = padding
        for _layout in self._layouts.values():
            if len(_layout) > longest:
                longest = len(_layout)
        for _layout in self._layouts.values():
            _layout.set_padding(longest)
