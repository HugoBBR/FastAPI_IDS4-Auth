# Introduction

This is for the IT OS API built in FastAPI.

# Setup for Mac

python3 -m venv .venv
source .venv/bin/activate

# pip install -r requirements.txt --force-reinstall --upgrade

# pip install --force-reinstall "fastapi[all]"

# For Windows

python3 -m venv .venv
.venv\Scripts\activate.ps1

Install the requirements file
pip install -r requirements.txt
pip install -r requirements-local.txt

# To run locally

uvicorn main:app --reload

# To Clean Code before commit

## All at once

black . && isort --profile black . && flake8 .

run _black ._ to format all files or directories
run _isort --profile black ._ and this will sort imports "standard library/third-party/local"
run _flake8 ._ and FIX all errors

# To TEST before commit

run _pytest_ in your terminal in the same directory
run _pytest --lf_ run last failed tests

pytest --junitxml=junit/test-results.xml

# To Test Code Coverage

pip install pytest-cov
-- Only to test coverage for the routers
pytest --cov="./routers" --cov-report html

# To test security

pip install bandit
bandit routers -r

# To test for package dependencies Security

pip install safety
safety check
