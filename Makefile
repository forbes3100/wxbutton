# Makefile for building wxPython application with py2app

PYTHON = python3.10
SOURCE = wxbutton.py
APP_NAME = wxButton.app

all: dist/$(APP_NAME)

dist/$(APP_NAME): setup.py $(SOURCE) | dist
	$(PYTHON) setup.py py2app

dist:
	mkdir -p dist

clean:
	$(PYTHON) setup.py clean
	rm -rf build dist *.egg-info
