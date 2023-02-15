from prettypy.layout import Layout

DEFAULT_LAYOUTS = {
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
    "note": {
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
    def __init__(self) -> None:
        """
        Initialize Composer.
        """
        self._layouts = {}
        self.add_layouts(DEFAULT_LAYOUTS)

    def add_layouts(self, layouts: dict) -> None:
        """
        Add multiple Layouts to the composer,
        by passing a dictionary with styling instructions.
        :param layouts: Layouts to add

        Note:
        Layouts must be in the following format:
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
            layout = Layout(_name)
            layout.set_prefix(_layout["prefix"][0], _layout["prefix"][1],
                              _layout["prefix"][2], _layout["prefix"][3])
            layout.set_text(_layout["text"][0], _layout["text"][1],
                            _layout["text"][2], _layout["text"][3])
            layout.set_suffix(_layout["suffix"][0], _layout["suffix"][1],
                              _layout["suffix"][2], _layout["suffix"][3])
            self._layouts[_name] = layout

    def add(self, name: str, text: str, color: str = "reset") -> None:
        """
        Add a simple layout to the composer.
        :param name: Name of the layout
        :param text: Text to use
        :param color: Color to use

        Example:
            composer.add_simple_layout("test", "[Test]", "red")
        """
        layout = Layout(name)
        layout.set_prefix("", color, "reset", "reset")
        layout.set_text(text, color, "reset", "reset")
        layout.set_suffix("", color, "reset", "reset")
        self._layouts[name] = layout

    def remove_layout(self, name: str) -> None:
        """
        Remove a layout from the composer.
        :param name: Name of the layout to remove
        """
        self._layouts.pop(name)

    def get_layout(self, name: str) -> Layout:
        """
        Get a layout from the composer.
        :param name: Name of the layout to get
        """
        return self._layouts.get(name)

    def list_layouts(self) -> list:
        """
        List all layouts.
        """
        return list(self._layouts.keys())

    def compose(self, layout: str, msg: str = None) -> str:
        """
        Compose a text with a layout.
        :param layout: Name of the layout to use
        :param msg: Text to compose
        """
        layout = self.get_layout(layout)
        return layout.render(msg)

    def print(self, layout: str, msg: str = None) -> None:
        """
        Compose a text with a layout and print it.
        :param layout: Name of the layout to use
        :param msg: Text to compose
        """
        print(self.compose(layout, msg))

    def adjust_padding(self, padding: int = 0) -> None:
        """
        Adjust the padding of all layouts.
        :param padding: Padding to use if the longest layout
            is shorter than the padding
        """
        longest = padding
        for _layout in self._layouts.values():
            if _layout.get_effective_length() > longest:
                longest = _layout.get_effective_length()
        for _layout in self._layouts.values():
            _layout.set_padding(longest)


if __name__ == '__main__':
    composer = Composer()
    composer.add("test", "[Test]", "red")
    print(composer.compose("error", "This is an error message"))
    composer.adjust_padding()
    print(composer.compose("success", "This is a success message"))
    print(composer.compose("test", "This is a test message"))
