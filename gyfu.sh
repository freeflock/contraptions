#!/bin/bash

. .venv/bin/activate
python3 setup.py sdist
twine upload --non-interactive --skip-existing dist/*
