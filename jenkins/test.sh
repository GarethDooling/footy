#!/bin/bash

source venv/bin/activate

python3 -m pytest \
	--cov=app \
    --cov-report term-missing \
    --cov-report xml:coverage.xml \
    --junitxml=junit_report.xml