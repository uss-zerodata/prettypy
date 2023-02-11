Update requirements.txt
~~~sh
python3 -m  pipreqs.pipreqs .
~~~

Build package
~~~sh
python .\setup.py sdist bdist_wheel
~~~

Publish to pypi
~~~sh
python -m twine upload dist/*
~~~
