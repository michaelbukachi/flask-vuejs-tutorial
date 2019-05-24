#!/usr/bin/env bash
pytest --cov-report term-missing:skip-covered --cov=app --capture=sys tests