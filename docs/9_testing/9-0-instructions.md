# Activities 9: Testing (unit testing and continuous integration in GitHub)

_*Theme: Working with code (for applications)*_ 

This is the final set of activities for COMP0035.

## Pre-requisites

Before starting, check you:

1. Configured your IDE to support pytest:

    - [Pycharm help: Testing frameworks](https://www.jetbrains.com/help/pycharm/testing-frameworks.html)
    - [Python testing in VS Code](https://code.visualstudio.com/docs/python/testing)
2. Installed `pytest` and `pytest-cov` in your venv `pip install pytest pytest-cov`
3. [Pytest good practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html) recommends you install your
   project code in your virtual environment (venv) using 

    `pip install -e .` 

    Check that you updated your pyproject.toml if you changed your code directory structure or name.

## Complete the activities

Instructions and activities can be found in the docs/9_testing folder:

1. [Introduction to testing and conventions](9-01-introduction.md)
2. [Testing with pytest](9-02-pytest-tests.md)
3. [Pytest fixtures](9-03-fixtures.md)
4. [Reporting test coverage](9-04-coverage.md)
5. [Running tests with GitHub Actions](9-05-ci-github.md)
6. [Further information](9-06-further.md)

[Next activity](9-01-introduction.md)