from models import Post

def test_postModel():
    PostSample = Post('Sample post', 'This is a test', 'Final View', 'Nujabes', 'this is not a link')

    assert PostSample.title == 'Sample post'
    assert PostSample.caption == 'This is a test'
    assert PostSample.song_name == 'Final View'
    assert PostSample.song_artists == 'Nujabes'
    assert PostSample.song_link == 'this is not a link'