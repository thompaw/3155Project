# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
from flask import Blueprint, abort, redirect, render_template, request, session
from sqlalchemy import null
from models import Comment, Post, Userprofile, db
import spot

router = Blueprint('Post_router', __name__, url_prefix='/post')

@router.get('') #TODO: output all posts in reverse order for main feed
def get_all_Post():
    all_posts = Post.query.all()
    
    users = []
    for post in all_posts:
        users.append(Userprofile.query.get(post.user_id))
        print(post.user_id)
    
    all_posts.reverse()
    users.reverse()
    
    return render_template('all_posts.html', posts = all_posts, user_in_session = session['user']['user_id'], currentuser = Userprofile.query.get(session['user']['user_id']), users=users)

@router.get('/<post_id>') #TODO: output single post
def get_single_Post(post_id):
    single_post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post_id).all()
    commentUsernames=[]
    for comment in comments:
        commentUsernames.append(Userprofile.query.get(comment.user_id))
    
    user = Userprofile.query.get_or_404(single_post.user_id)
    print(comments)
    return render_template('single_post.html', post = single_post, comments=comments, usernames=commentUsernames, postuser = user, user_in_session = session['user']['user_id'])


@router.post('') #TODO: create post with spotify implementation!!
def create_post():
    #post_id = Post.query.get_or_404(post_id)
    user_id = session['user']['user_id'] #get user session id
    title = request.form.get('post_title', '')
    caption = request.form.get('post_caption', '')
    song = request.form.get('song_select', '')
    song = spot.single(song)

    song_name = song['name']
    artists = song['artists']
    artiststring = ''
    song_image = song['album']['images'][0]['url']
    
    for x,artist in enumerate(artists):
        artiststring = artiststring + artist['name']
        if x != len(artists)-1:
            artiststring = artiststring + ', '
    song_link = song['preview_url']

    if title == '' or song_name == '' or caption == '' or song_link == '' or artiststring== '':
        abort(400)

    new_post = Post(user_id=user_id, title=title, caption=caption, song_name=song_name, song_artists=artiststring, song_link=song_link, song_image=song_image)
    db.session.add(new_post)
    db.session.commit()
    return redirect(f'/post/{new_post.post_id}')   



@router.get('/<post_id>/edit') #TODO:edit parts of the title
def get_edit_Post_form(post_id):
    post_to_edit = Post.query.get_or_404(post_id)
    return render_template('editpost.html', post = post_to_edit, user_in_session = session['user']['user_id'])     

@router.post('/<post_id>') #TODO: do the updating for the post
def update_post(post_id):
    post_to_update = Post.query.get_or_404(post_id)
    title = request.form.get('title', '')
    caption = request.form.get('caption', '')

    if title == '' or caption == '':
        abort(400)

    post_to_update.title = title
    post_to_update.caption = caption

    db.session.commit()
    return redirect(f'/post/{post_id}')

@router.post('/<post_id>/delete') #TODO: delete a post
def delete_post(post_id):
    post_to_delete = Post.query.get_or_404(post_id)
    comments_to_delete = Comment.query.filter_by(post_id=post_id).all()
    for comment in comments_to_delete: #you have to delete all comments related to that post before deleting the post
        db.session.delete(comment)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect('/post')
