# Local install

Install package locally for testing
~~~sh
pip install .
~~~

# Test

Run tests
~~~sh
python -m pytest
~~~

# Lint

Lint code
~~~sh
python -m flake8
~~~

# Docs
    
Generate docs
~~~sh
python -m pdoc --output-dir docs prettypy/
~~~

Preview docs
~~~sh
python -m http.server --directory docs
~~~

# Requirements

Update requirements.txt
~~~sh
python3 -m  pipreqs.pipreqs .
~~~

# Clean

Clean build files
~~~sh
rm -rf build dist *.egg-info
~~~

# Version

Update version
~~~sh
python -m bump2version patch
~~~

# Build

Build package
~~~sh
python -m build
~~~

# Publish Test

Get package name from setup.cfg and set environment variable
~~~sh
export PACKAGE_NAME=$(grep -oP '(?<=name = ).*' setup.cfg)
~~~

Publish package to test pypi
~~~sh
python3 -m twine upload --repository testpypi dist/*
~~~

Uninstall package
~~~sh
pip uninstall $PACKAGE_NAME
~~~

Test install
~~~sh
pip install -i https://test.pypi.org/simple/ $PACKAGE_NAME
~~~

# Publish

Publish package to pypi
~~~sh
python3 -m twine upload --repository pypi dist/*
~~~

---

[video source](https://www.youtube.com/watch?v=JkeNVaiUq_c)