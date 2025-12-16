# 7. Going further

## Paralympics example tests

This week's lecture included a demo of unit testing using pytest for a model class for the
paralympics database. These tests are included in [paralympics](../../tests/paralympics).

There are also tests that use a pytest fixture with an instance of a database. The fixture is used
in tests for a query class.

## Further information

There is more to unit testing with Pytest than can be covered in one tutorial.

If you are interested, investigate other aspects such as:

- tests
  for [error conditions (exceptions)](https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertions-about-expected-exceptions)
- edge/boundary cases i.e. handling extreme values of valid limits, and just beyond ([pytest-with-eric tutorial](https://pytest-with-eric.com/introduction/python-testing-strategy/#Boundary-Conditions))
- [organising tests in classes](https://stackoverflow.com/questions/50016862/grouping-tests-in-pytest-classes-vs-plain-functions) rather than functions.
- [parameterised tests](https://docs.pytest.org/en/latest/how-to/parametrize.html)
- [doctests using the docstrings](https://realpython.com/python-doctest/)
- use of
  mocks - e.g. [pytest-with-eric tutorial](https://pytest-with-eric.com/pytest-advanced/pytest-mocking/)

Other tutorials:

- [RealPython: Effective testing with Python](https://realpython.com/pytest-python-testing/)
- [freeCodeCamp: Python testing for beginners (video)](https://www.youtube.com/watch?v=cHYq1MRoyI0) -
  includes mocks and
  using ChatGPT for testing