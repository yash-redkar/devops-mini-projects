# Mini Project 04: CI Pipeline for Python App

## Project Overview

This mini project demonstrates a Continuous Integration pipeline for a Python application using GitHub Actions.

The project contains a simple Student Grade Calculator application, unit tests using pytest, code linting using flake8, and a coverage report using pytest-cov.

The CI pipeline runs automatically on every push and pull request to the main branch.

## Features

* Python-based Student Grade Calculator
* Calculates average marks
* Assigns grade based on average marks
* Takes user input when running manually
* Unit testing with pytest
* Code linting with flake8
* Test coverage report with pytest-cov
* GitHub Actions workflow for CI automation
* 100% test coverage for core application logic

## Tech Stack

* Python
* pytest
* flake8
* pytest-cov
* GitHub Actions
* Git
* GitHub

## Project Structure

```text
mini-project-04-ci-pipeline-python-app/
│
├── app.py
├── test_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

The GitHub Actions workflow is stored in the root repository path:

```text
.github/workflows/python-ci.yml
```

## How to Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Example input:

```text
65,76,89,90
```

Example output:

```text
Student Grade Calculator
Average Marks: 80.0
Grade: B
```

## Run Linting

```bash
flake8 app.py test_app.py
```

If there is no output, linting has passed successfully.

## Run Unit Tests

```bash
pytest
```

## Run Tests with Coverage

```bash
pytest --cov=app --cov-report=term-missing
```

Expected result:

```text
8 passed
TOTAL 100%
```

## GitHub Actions CI Pipeline

The CI workflow runs automatically on:

* Push to main branch
* Pull request to main branch

The pipeline performs the following steps:

1. Checkout source code
2. Set up Python
3. Install dependencies
4. Run flake8 linting
5. Run pytest unit tests
6. Generate coverage report

## Success Outcome

A Python application with automated quality checks using GitHub Actions.

The project includes:

* Working Python script
* Unit tests
* Linting
* Coverage report
* Automated CI pipeline
* Green GitHub Actions build

## Author

Yash Redkar

