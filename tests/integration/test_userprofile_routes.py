def test_create_user(test_app):
    res = test_app.post('/signup', data=
    {
        'username' : 'ReallyCool1',
        'user_id' : 1
    }, follow_redirects = True)  

    assert res.status_code == 200
    assert b'ReallyCool1' in res.data
    assert b'1' in res.data

# def test_get_all_users(test_app):
#     res = test_app.get('/user_profile')

#     assert res.status_code == 401                   # not logged in so you should have no access (ie. 401)


# def test_get_all_cats(test_app):                        # test_app from conftest.py does the backwiring
#     res = test_app.get('/cats')

#     assert res.status_code == 200                       # Status code is good
#     assert b'No CATS! Go make a CAT.' in res.data


    
# def test_create_cat(test_app):
#     res = test_app.post('/cats', data={                  # Make a cat to add to database to check if it is true
#         'name' : 'Piano',
#         'breed' : 'Orange',
#         'numLegs' : 4
#     }, follow_redirects = True)                         # Allows test to follow the redirect

#     assert res.status_code == 200
#     assert b'Piano' in res.data
#     assert b'Orange' in res.data
#     assert b'4' in res.data