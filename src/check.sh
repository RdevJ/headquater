#! /usr/bin/env sh

set -e
set -x

echo "flake8..."
flake8 app/

# echo "mypy..."
# mypy app/

echo "bandit..."
bandit -r app/ -x app/api/v1/endpoints/tests

echo "xenon..."
xenon app/

echo "safety..."
safety check --full-report --bare