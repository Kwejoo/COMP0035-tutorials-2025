# 3. Using Pytest fixtures

If you find yourself writing tests where you use the same set-up ('arrange') steps, you can create
reusable 'fixtures'.

[Pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.htmle) are used to provide
common functions that you may need for your tests. They are created (set up, yield) and removed 
(tear down, finalise) using the `@fixture` decorator.

Fixtures are established for a particular scope using the syntax `@pytest.fixture(scope='module')`.
Options for scope are:

- `function` fixture is executed/run once per test function (if no scope is specified then this is
  the default)
- `class` one fixture is created per class of tests (if creating test classes)
- `module` fixture is created once per module (e.g., a test file)
- `session` one fixture is created for the entire test session

You may not need to use fixtures for COMP0035 coursework, however, you will need to use in COMP0034,
so it is a good idea to learn and practice now.

Fixtures can be added either within the test file (module) or in a separate python file called
`conftest.py`. Placing them in `conftest.py` to make them available to other test modules. 
`conftest.py` is typically placed in the root of the `tests` directory, though you can have multiple 
`conftest.py` files (not covered here).

## Activity: Create a fixture

The tests `test_deal_hand_return_amount()` and `test_deck_cards_count()` both need a deck of cards
to be created.

It would be useful to create a fixture that creates a deck of cards that can be used by tests that
need it.

1. Add code to create the following fixture in `tests/conftest.py`:

```python
import pytest
from activities.starter.playing_cards import Suit, Rank, Deck


@pytest.fixture
def deck_cards():
    suit_values = [Suit(suit=s) for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']]
    rank_values = [Rank(rank=str(r)) for r in
                   [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']]
    deck_cards = Deck(suits=suit_values, ranks=rank_values)
    yield deck_cards
```

## Activity: Modify the tests to use the fixture

Update the code in the test module so that the test functions use the fixture.

You can pass a fixture to the function like this: `def test_query_select_succeeds(db):` where a
fixture called `db` is being passed to the function.

1. Modify the `test_deck_cards_count()` test function to use the fixture.

    ```python
   def test_deck_cards_count(deck_cards):
        # Arrange: deck_cards now comes from the fixture
        deck_length = len(deck_cards.deck)  # Act
        assert deck_length == 52  # Assert
    ```

2. Repeat for the `test_deal_hand_return_amount()` test.

3. Run the tests and check the output.

## Database fixtures

Although a test that relies on an external component such as a database is not considered a unit
test, it is still a test.

You will be using databases in COMP0034.

You would not want tests to change data in a live database, so you would create a temporary
database.

For small databases like the card database, you can create a database in memory, i.e. that is not
stored as a file.

The database can then be recreated for each test so that any changes to the database from one test
don't impact another.

The [SQLModel example](https://sqlmodel.tiangolo.com/tutorial/fastapi/tests/?h=test#pytest-fixtures)
shows a fixture which can be adapted for the cards database:

```python
import pytest
from sqlmodel import create_engine, SQLModel, Session
from sqlmodel.pool import StaticPool

from activities.starter.playing_cards import create_cards


@pytest.fixture(name="session")
def session_fixture():
    # Create the cards
    suits, ranks, cards = create_cards()

    # Create the session and yield
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        # Add the objects to the database
        session.add_all(suits)
        session.add_all(ranks)
        session.add_all(cards)
        session.commit()
        yield session
```

### Activity: Create and use a database fixture

The following code is in [test_playing_cards.py](../../tests/playing_cards/test_playing_cards.py):

```python
def test_select_returns_cards():
    """ Test that database returns results when the cards table is queried
    
    GIVEN an existing database in memory
    WHEN a query is made to the cards table
    THEN it should return a result set with 52 rows
    """
    db_path = ":memory:"
    engine = create_cards_db(db_path=db_path)
    with Session(engine) as session:
        statement = select(CardModel)
        result = session.exec(statement)
        cards = result.all()
        assert len(cards) == 52
```

1. Create a fixture that returns the session
2. Modify `test_select_returns_cards()` to use the session fixture
3. Run the test and check it works

[Next activity](9-04-coverage.md)