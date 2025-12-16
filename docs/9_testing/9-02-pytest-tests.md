# 2. Writing unit tests with Pytest

## Test case structure

Given the guidance in the introduction, here is a suggested approach for writing a unit test:

1. **Write a descriptive test function name**

    - Test functions should start with the prefix `test_`.
    - Use a name that clearly describes what is being tested e.g. `test_add_success_with_integers` is more informative
      than `test_add`, as it describes both the function and the behaviour being tested.

2. **Add a docstring**.

   Consider include a description that uses the 'GIVEN > WHEN > THEN' pattern to clearly document the purpose of the
   test.

    ```python
   def test_valid_email():
    """
        GIVEN valid values an Admin object, email='test@test.com' and password='testpassword'
        WHEN the Admin object 'admin' is created
        THEN admin.email should equal 'test@test.com'
    """
    ```

3. **Arrange**: Set up the test conditions

    - Provide the necessary values or objects e.g. `email = 'test@test.com`, `password = 'testpassword'`

4. **Act**: Call the function or method being tested:

    - e.g. `admin = Admin(email, password)`

5. **Assert**: Check that the result is as expected.

    - Use an assertion to verify the outcome e.g. `assert admin.email == email`

6. **Run the test** and check that it passes.

    - There are different ways to run tests:

        - [VS Code green run icon](https://code.visualstudio.com/docs/python/testing#_run-tests)
        - [PyCharm green run icon](https://www.jetbrains.com/help/pycharm/pytest.html#create-pytest-test)
        - Add command to a main() function
        - From the command line in the venv terminal. If you run `pytest -v` it
          will look for all the tests it can autodiscover and run them. You can specify folders, modules or even
          specific test functions, e.g.: `pytest -v tests/test_modulename.py::test_valid_email`

These activities give command line instructions only, but you can use any method.

An example is in [test_playing_cards.py](../../tests/playing_cards/test_playing_cards.py).

## Testing errors and exceptions

Write assertions that are expected to pass.

Don't write assertions just to make them fail deliberately.

The purpose of a test is to verify that the code behaves as expected. A test should only fail if there is an actual
issue with the code being tested.

Writing tests that are designed to fail can be confusing and misleading, unless you're specifically testing error
handling or failure scenarios—and even then, the assertion should still reflect the expected behaviour in that context.

For example, **do not** write tests like this:

```python
def test_addition_with_invalid_data():
    """
    GIVEN two string values 'a' and 'b'
    WHEN they are passed to an addition function expecting integers
    THEN the test will fail because the input is invalid
    """
    # Arrange
    a = "a"
    b = "b"

    # Act
    result = a + b  # This will succeed in Python, but it's not meaningful for an integer addition function

    # Assert
    assert result == 2  # This will fail because 'a' + 'b' results in 'ab', not 2
```

The syntax
to [test exceptions](https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertions-about-expected-exceptions) is
different.

Example from the `pytest` documentation:

```python
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

Given this, the bad test example above is rewritten as:

```python
import pytest

import pytest


def test_add_raises_type_error_on_strings():
    """
    GIVEN two string inputs 'a' and 'b'
    WHEN passed to the add() function
    THEN a TypeError should be raised
    """
    # Arrange
    a = "a"
    b = "b"

    # Act & Assert
    with pytest.raises(TypeError):
        add(a, b)
```

## Activities

### 1. Run a test

1. Look at the code in [test_playing_cards.py](../../tests/playing_cards/test_playing_cards.py).

   It contains:

    - `Rank` and `Suit`: SQLModel classes that store the suit and rank values used in playing cards
    - `Deck`: a Python class functions including `deal`, `shuffle`, etc.
    - `create_cards_db`: a Python function that creates database with Rank and Suit and saves to the test folder. It
      returns
      an error if the database is not created.

2. Run the test and check it passes: `pytest -v tests/test_playing_cards.py::test_suit_returns_suitstring`

### 2. Run a test that fails

You want all tests to pass. If a test fails, read the output to try and identify the problem.

1. Run the test using the option `-v` which gives a more detailed test output
   `pytest -v tests/test_playing_cards.py::test_suit_returns_suitstring`
2. Read the output and try to work out what the error message is telling you
3. Fix the bug in the code and re-run the test. Did it pass?

### 3. Write a test

1. Complete the code for `test_deck_cards_count()`
2. Run the test and check if it passes

Add at least one more test, e.g., one for the Rank class similar to Suit, or test one of the methods of the Deck class.
Try to write unit tests if you can.

### 4. Write a test that raises an exception

1. Complete the code for `test_create_cards_db_raises_on_invalid_path()`
2. Run the test and check if it passes

### 5. Use IDE or Copilot to generate a unit test

If you have copilot enabled in your IDE, try generating a test automatically.

Right-click on a class or function name in the code and find the option to generate a test:

- PyCharm: Generate... | Test
- VS Code: Copilot | Generate tests...

Review the generated code. Do you agree with it?

Run the tests and see if they run.

## Further practice

If you want to practice further, write tests for some of the paralymics model classes or functions 
created in earlier activities (e.g. data prep in week 2, database in week 4, classes in week 5).

[Next activity](9-03-fixtures.md)