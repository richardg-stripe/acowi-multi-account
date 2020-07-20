install:
	poetry install

clone_example:
	poetry run python clone_example.py

clone_example_headers:
	poetry run python clone_example_headers.py

setup:
	poetry run python setup.py