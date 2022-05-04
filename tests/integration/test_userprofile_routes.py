def test_get_all_users(test_app):
    res = test_app.get('/user_profile')

    assert res.status_code == 200                   # not logged in so you should have no access (ie. 401)

