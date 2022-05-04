import pytest

from app import app

from flask import session

@pytest.fixture(scope='module')
def test_app():
    with app.test_client() as test_app:
        session['user'] = {
            'username': 'ReallyCool1',
            'user_id': 1
        }
        yield test_app