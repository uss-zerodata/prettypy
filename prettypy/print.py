def __init__(self, *args, **kwargs):
    self._print = print
    self._print(*args, **kwargs)


def _print(self, *args, **kwargs):
    print(*args, **kwargs)
