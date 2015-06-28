
PACKAGE="caesar"
VERSION = $(shell cat setup.py | grep version | sed -e "s/version=//" -e "s/'//g" -e "s/,//" -e 's/^[ \t]*//')
PYTHON_EXEC=python
PYTHON3_EXEC=python3
PIP_EXEC=pip

install:
	@echo "Creating distribution package for version $(VERSION)"
	@echo "-----------------------------------------------"
	$(PYTHON3_EXEC) setup.py sdist
	@echo "Installing package using $(PIP_EXEC)"
	@echo "----------------------------"
	$(PIP_EXEC) install --upgrade dist/$(PACKAGE)-$(VERSION).tar.gz

clean:
	find . -type f -name '*.pyc' -exec rm {} +
	find . -type d -name '__pycache__' -exec rm -r {} +
