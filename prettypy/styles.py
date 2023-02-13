from prettypy.color import Color


class Styles:
    styles: dict = {
        "default": {
            "text": "",
            "foreground": "reset",
            "background": "reset",
            "format": "reset",
            "render": "",
            "render_len": 0
        }
    }

    _default_styles: dict = {
        "default": {
            "text": "",
            "foreground": "reset",
            "background": "reset",
            "format": "reset"
        },
    }

    def __init__(self):
        """
        Initialize the styles class.
        """
        for style in self._default_styles:
            self.set_style(
                style, self._default_styles[style]["text"],
                self._default_styles[style]["foreground"],
                self._default_styles[style]["background"],
                self._default_styles[style]["format"]
            )

    def __call__(self, name: str) -> str:
        """
        Get a format from the 'styles' dict.
        :param name: Name of the format to get
        :return: Rendered format
        """
        return self.get_style(name)

    def __getitem__(self, name: str) -> str:
        """
        Get a format from the 'styles' dict.
        :param name: Name of the format to get
        :return: Rendered format
        """
        return self.get_style(name)

    def __setitem__(self, name: str, value: dict) -> None:
        """
        Set a format in the 'styles' dict.
        :param name: Name of the format to set
        :param value: Style information
        """
        self.set_style(name, value["text"], value["foreground"], value["background"], value["format"])

    def __delitem__(self, name: str) -> None:
        """
        Delete a format from the 'styles' dict.
        :param name: Name of the format to delete
        """
        del self.styles[name]

    def __contains__(self, name: str) -> bool:
        """
        Check if a format exists in the 'styles' dict.
        :param name: Name of the format to check
        :return: True if the format exists, False if it doesn't
        """
        return name in self.styles

    def __len__(self) -> int:
        """
        Get the length of the 'styles' dict.
        :return: Length of the 'styles' dict
        """
        return len(self.styles)

    def __iter__(self) -> iter:
        """
        Iterate over the 'styles' dict.
        :return: Iterator
        """
        return iter(self.styles)

    def __repr__(self) -> str:
        """
        Get the representation of the 'styles' dict.
        :return: Representation of the 'styles' dict
        """
        return repr(self.styles)

    def __str__(self) -> str:
        """
        Get the string representation of the 'styles' dict.
        :return: String representation of the 'styles' dict
        """
        return str(self.styles)

    def __bool__(self) -> bool:
        """
        Get the boolean representation of the 'styles' dict.
        :return: Boolean representation of the 'styles' dict
        """
        return bool(self.styles)

    def __eq__(self, other: dict) -> bool:
        """
        Check if the 'styles' dict is equal to another dict.
        :param other: Other dict to check
        :return: True if the dicts are equal, False if they aren't
        """
        return self.styles == other

    def __ne__(self, other: dict) -> bool:
        """
        Check if the 'styles' dict is not equal to another dict.
        :param other: Other dict to check
        :return: True if the dicts are not equal, False if they are
        """
        return self.styles != other

    def get_styles_list(self) -> list:
        """
        Get a list of all styles.
        :return: List of all styles
        """
        return list(self.styles.keys())

    def set_style(self, name: str, text: str, _fg: str = None, _bg: str = None, _style: str = None) -> None:
        """
        Set a format in the 'styles' dict.
        :param name: Name of the format to set
        :param text: Prefix to use for the format
        :param _fg: Foreground color
        :param _bg: Background color
        :param _style: Style to apply

        Example:
        styles.set_style("error", "[ERROR]", "red", "black", "bold")
        """
        render = Color.colorize(text, _fg, _bg, _style)
        self.styles[name] = {
            "text": text,
            "foreground": _fg,
            "background": _bg,
            "format": _style,
            "render": render,
            "render_len": len(render)
        }

    def get_style(self, name: str) -> str:
        """
        Get a format from the 'styles' dict.
        :param name: Name of the format to get
        :return: Rendered format
        """
        return self.styles[name]["render"]

    def get_style_raw(self, name: str) -> dict:
        """
        Get a format from the 'styles' dict.
        :param name: Name of the format to get
        :return: Raw format information
        """
        return self.styles[name]

    def remove_style(self, name: str) -> None:
        """
        Remove a format from the 'styles' dict.
        :param name: Name of the format to remove
        """
        del self.styles[name]
