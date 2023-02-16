import unittest
from io import StringIO
from unittest.mock import patch

from prettypy.pretty import Pretty


class TestPretty(unittest.TestCase):
    def test__init__(self):
        pretty = Pretty()
        self.assertEqual(pretty._composer._no_color,
                         False, "No color should be False")
        pretty = Pretty(no_color=True)
        self.assertEqual(pretty._composer._no_color,
                         True, "No color should be True")

    def test__call__(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("neutral", "test"), "Should be equal")

    def test_info(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.info("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("info", "test"), "Should be equal")

    def test_success(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.success("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("success", "test"), "Should be equal")

    def test_warning(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.warning("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("warning", "test"), "Should be equal")

    def test_error(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.error("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("error", "test"), "Should be equal")

    def test_debug(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.debug("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("debug", "test"), "Should be equal")

    def test_notice(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.notice("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("notice", "test"), "Should be equal")

    def test_log(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.log("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("log", "test"), "Should be equal")

    def test_question(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.question("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("question", "test"), "Should be equal")

    def test_positive(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.positive("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("positive", "test"), "Should be equal")

    def test_negative(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.negative("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("negative", "test"), "Should be equal")

    def test_neutral(self):
        pretty = Pretty()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            pretty.neutral("test")
            self.assertEqual(fake_out.getvalue().strip(),
                             pretty._composer.compose("neutral", "test"), "Should be equal")

    def test_get_composer(self):
        pretty = Pretty()
        self.assertEqual(pretty.get_composer(),
                         pretty._composer, "Should be equal")
