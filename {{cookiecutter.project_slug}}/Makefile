all: lint test clean

VENV_ACTIVATE = source .venv/bin/activate
PYTHON = python3.11

.PHONY: lint test clean dev stable publish docs

lint:
	git add .
	$(VENV_ACTIVATE); pre-commit run

test:
	$(VENV_ACTIVATE); pytest tests -n auto --disable-warnings --show-capture=no

clean:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.py[co]' -delete
	find . -type f -name '*~' -delete
	find . -type f -name '.*~' -delete
	rm -rf .cache .pytest_cache .mypy_cache htmlcov *.egg-info
	rm -f .coverage .coverage.*
	rm -rf .tox build .idea

dev:
	$(PYTHON) -m venv .venv
	$(VENV_ACTIVATE); \
	pip install setuptools wheel; \
	pip install -U pip; \
	pip install -e ".[tests]"; \
	pip install pre-commit tox

stable:
	git checkout main
	git branch -D stable
	git checkout -b stable
	git push origin head -f
	git checkout main

.PHONY: publish
publish:
	$(VENV_ACTIVATE); python -m pip install --upgrade pip build twine; python -m build; python -m twine upload dist/*

.PHONY: docs
docs:
	$(VENV_ACTIVATE); pip install -e .[docs]; mkdocs serve

