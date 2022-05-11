from models import Comment

def test_comment_model():
    Testcomment = Comment('Sample content')

    assert Testcomment.content == 'Sample content'