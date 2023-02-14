# class Style

Data structure for storing style information.

- FOREGROUND: dict
- BACKGROUND: dict
- FORMAT: dict
- stylize(text, foreground, background, format)

# Layout

Data structure for storing layout information.

- Layout
  - prefix
    - foreground
    - background
    - text_style
  - text
    - foreground
    - background
    - text_style
  - suffix
    - foreground
    - background
    - text_style
  - set_prefix()
  - set_text()
  - set_suffix()
  - render()

# class Composer

Data structure for storing layout information.

- Composer
  - default_layouts
  - layouts
  - __init__()
  - __iter__()
  - list_layouts()
  - add_layout()
  - remove_layout()
  - get_layout()
  - render()

# class PrettyPy

Main class for PrettyPy.

- pretty
  - __call__(mode, text, prefix, suffix)
  - info(text, prefix, suffix)
  - success(text, prefix, suffix)
  - warning(text, prefix, suffix)
  - error(text, prefix, suffix)
  - debug(text, prefix, suffix)
  - note(text, prefix, suffix)
  - log(text, prefix, suffix)
  - question(text, prefix, suffix)
  - positive(text, prefix, suffix)
  - negative(text, prefix, suffix)
  - neutral(text, prefix, suffix)
  - highlight(text, prefix, suffix)
  - emphasize(text, prefix, suffix)
  - bold(text, prefix, suffix)
- progress
  - __init__(text, prefix, suffix, total, status)
  - start(percent, status)
  - update(percent, status)
  - stop()
