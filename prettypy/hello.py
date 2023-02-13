
def say_hello() -> str:
    """
    This function prints "Hello World" and returns "Hello World!".
    :return: "Hello World!"
    """
    print("Hello World")
    return "Hello World!"

def main():
    """
    This function calls the say_hello function.
    :return: None
    """
    say_hello()

def test_say_hello():
    """
    This function tests the say_hello function.
    :return: None
    """
    assert say_hello() == "Hello World!"
