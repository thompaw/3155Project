from models import Userprofile

def test_userprofile_model():
    u = Userprofile('ReallyCool1', 'abc123', 'ReallyCool1@gmail.com')

    assert u.user_name == 'ReallyCool1'
    assert u.user_password == 'abc123'
    assert u.user_email == 'ReallyCool1@gmail.com'
    assert u.user_biography == None
    assert u.user_location == None