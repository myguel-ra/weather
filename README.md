# Weather Prediction API
![Python Versions](https://img.shields.io/badge/Python-3.11-blue.svg)

Welcome to my Weather API Demo! This Python project uses FastAPI to expose endpoints for predicting temperature and rainfall .

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Running Tests](#running-tests)
- [Development](#development)
  - [Setting Up Poetry](#setting-up-poetry)
  - [Running Tests with Coverage](#running-tests-with-coverage)
  - [Using Pre-commit Hooks](#using-pre-commit-hooks)
  - [Creating Releases](#creating-releases)
- [More Information](#more-information)
  - [Project Dependencies](#project-dependencies)
  - [License](#license)

## Requirements

Ensure you have the following software installed on your machine:

- [Python](https://www.python.org/) (version 3.11)
- [Poetry](https://python-poetry.org/) (for managing dependencies)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/weather.git
    ```

2. Navigate to the project directory:

    ```bash
    cd weather
    ```

3. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

## Usage

### Running the Application

To start the FastAPI application with Uvicorn:

```bash
poetry run uvicorn api.main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000). Explore the Swagger documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Running Tests

To run tests with pytest:

```bash
poetry run pytest
```

## Development

### Setting Up Poetry

Ensure you have [Poetry](https://python-poetry.org/docs/) installed. If not, you can install it using:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```
or
```bash
pip install poetry
```

### Running Tests with Coverage
To run tests with coverage using pytest-cov:

```bash
poetry run pytest --cov
```

### Using Pre-commit Hooks
This project uses pre-commit hooks to ensure code quality. Install pre-commit using:

```bash
pre-commit install
```
The hooks will run automatically before each commit.

```bash
pre-commit run --all-files
```
Also, hooks can be triggered manually

### Creating Releases
Follow these steps to create a new release:

Update the version in pyproject.toml.

Run the following command to generate a new distribution:

```bash
poetry build
```

## More Information
### Project Dependencies
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pre-Commit](https://pre-commit.com/)

## License
This project is licensed under the [Apache License, Version 2.0](LICENSE).
