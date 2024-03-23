all: lint test clean

.PHONY: dev
dev:
	python3.10 -m venv .venv
	source .venv/bin/activate; pip install -e .[tests]; pip install pre-commit

.PHONY: lint
lint:
	git add .
	source .venv/bin/activate; pre-commit run --all-files

.PHONY: test
test:
	source .venv/bin/activate; pytest tests -x -v --disable-warnings --show-capture=no

.PHONY: tox
tox:
	tox

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf *.egg-info
	rm -f .coverage
	rm -f .coverage.*
	rm -rf .tox
	rm -rf build

.PHONY: push
push:
	git push origin head

.PHONY: amend
amend:
	git add .
	git commit --amend --no-edit
	git push origin head -f

.PHONY: stable
stable:
	git checkout main
	git branch -D stable
	git checkout -b stable
	git push origin head -f
	git checkout main

.PHONY: publish
publish:
	source .venv/bin/activate; python -m pip install --upgrade pip
	source .venv/bin/activate; python -m pip install --upgrade build
	source .venv/bin/activate; python -m pip install --upgrade twine
	source .venv/bin/activate; python -m build
	source .venv/bin/activate; python -m twine upload dist/*

.PHONY: docs
docs:
	source .venv/bin/activate; pip install -e .[docs]; mkdocs serve

.PHONY: sync-main
sync-main:
	git fetch --all
	git rebase origin/main
