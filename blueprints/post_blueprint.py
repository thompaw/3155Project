# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
from flask import Blueprint, abort, redirect, render_template, request
from models import Post, db
import spot

router = Blueprint('Post_router', __name__, url_prefix='/post')

@router.get('') #TODO: output all posts in reverse order for main feed
def get_all_Post():
    all_posts = Post.query.all()
    return render_template('all_posts.html', posts = all_posts)

@router.get('/<post_id>') #TODO: output single post
def get_single_Post(post_id):
    single_post = Post.query.get_or_404(post_id)
    return render_template('single_post.html', post = single_post)


@router.post('') #TODO: create post with spotify implementation!!
def create_post():
    #post_id = Post.query.get_or_404(post_id)
    user_id = 1 #get user session id
    title = request.form.get('post_title', '')
    caption = request.form.get('post_caption', '')
    song = request.form.get('song_select', '')
    song = spot.single(song)
    song_name = song['name']
    artists = song['artists']
    artiststring = ''
    
    for artist in artists:
        artiststring = artiststring + artist['name'] + ', '
    song_link = song['preview_url']
    #print(title + song_name + artiststring + caption + song_link)   

    if title == '' or song_name == '' or caption == '' or song_link == '' or artiststring== '':
        abort(400)

    new_post = Post(user_id=user_id, title=title, caption=caption, song_name=song_name, song_artists=artiststring, song_link=song_link)
    db.session.add(new_post)
    print("here")
    db.session.commit()
    return redirect(f'/post/{new_post.post_id}')   



@router.get('/<post_id>/edit') #TODO:edit parts of the title
def get_edit_Post_form(post_id):
    post_to_edit = Post.query.get_or_404(post_id)
    return render_template('editpost.html', post = post_to_edit)     

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
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect('/post')
