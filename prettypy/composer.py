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
    def __init__(self):
        """
        Initialize Composer.
        """
        self._layouts = {}
        self.add_layouts(DEFAULT_LAYOUTS)

    def add_layouts(self, layouts: dict):
        """
        Add multiple Layouts to the composer by passing a dictionary with styling instructions.
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
            layout.set_prefix(_layout["prefix"][0], _layout["prefix"][1], _layout["prefix"][2], _layout["prefix"][3])
            layout.set_text(_layout["text"][0], _layout["text"][1], _layout["text"][2], _layout["text"][3])
            layout.set_suffix(_layout["suffix"][0], _layout["suffix"][1], _layout["suffix"][2], _layout["suffix"][3])
            self._layouts[_name] = layout

    def remove_layout(self, name: str):
        """
        Remove a layout from the composer.
        :param name: Name of the layout to remove
        """
        self._layouts.pop(name)

    def get_layout(self, name: str):
        """
        Get a layout from the composer.
        :param name: Name of the layout to get
        """
        return self._layouts.get(name)

    def list_layouts(self):
        """
        List all _layouts.
        """
        return self._layouts.keys()

    def compose(self, layout: str, msg: str = None):
        """
        Compose a text with a layout.
        :param layout: Name of the layout to use
        :param msg: Text to compose
        """
        layout = self.get_layout(layout)
        return layout.render(msg)


if __name__ == '__main__':
    composer = Composer()
    print(composer.compose("error", "This is an error message"))
