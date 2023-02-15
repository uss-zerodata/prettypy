from prettypy.composer import Composer


class Pretty:
    def __init__(self) -> None:
        """
        Initialize Pretty.
        """
        self._composer = Composer()

    def __call__(self, msg: str) -> str:
        """
        Quick display message.
        :param msg: Message to display
        :return: Formatted text
        """
        return self.neutral(msg)

    def info(self, msg: str) -> str:
        """
        Display info message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("info", msg)
        print(pretty)
        return pretty

    def success(self, msg: str) -> str:
        """
        Display success message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("success", msg)
        print(pretty)
        return pretty

    def warning(self, msg: str) -> str:
        """
        Display warning message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("warning", msg)
        print(pretty)
        return pretty

    def error(self, msg: str) -> str:
        """
        Display error message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("error", msg)
        print(pretty)
        return pretty

    def debug(self, msg: str) -> str:
        """
        Display debug message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("debug", msg)
        print(pretty)
        return pretty

    def note(self, msg: str) -> str:
        """
        Display note message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("note", msg)
        print(pretty)
        return pretty

    def log(self, msg: str) -> str:
        """
        Display log message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("log", msg)
        print(pretty)
        return pretty

    def question(self, msg: str) -> str:
        """
        Display question message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("question", msg)
        print(pretty)
        return pretty

    def positive(self, msg: str) -> str:
        """
        Display positive message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("positive", msg)
        print(pretty)
        return pretty

    def negative(self, msg: str) -> str:
        """
        Display negative message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("negative", msg)
        print(pretty)
        return pretty

    def neutral(self, msg: str) -> str:
        """
        Display neutral message.
        :param msg: Message to display
        :return: Formatted text
        """
        pretty = self._composer.compose("neutral", msg)
        print(pretty)
        return pretty

    def get_composer(self) -> Composer:
        """
        Get composer instance.
        :return: Composer
        """
        return self._composer


if __name__ == '__main__':
    pretty = Pretty()
    pretty.info("Info message")
    pretty.success("Success message")
    pretty.warning("Warning message")
    pretty.error("Error message")
    pretty.debug("Debug message")
    pretty.note("Note message")
    pretty.log("Log message")
    pretty.question("Question message")
    pretty.positive("Positive message")
    pretty.negative("Negative message")
    pretty.neutral("Neutral message")
