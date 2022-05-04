import pytest
from app import app, db

# whenever test start: drop database, create local database (test.db), and with test_client() yeild it (magic to pass pytest)
@pytest.fixture(scope='module')
def test_app():
    with app.app_context(): 
        db.drop_all()                   # drops all previous items in database
        db.create_all()                 # look at model created and make a database inside of test.db

    with app.test_client() as test_app:
        yield test_app