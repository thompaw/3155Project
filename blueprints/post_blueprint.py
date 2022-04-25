# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
from flask import Blueprint, abort, redirect, render_template, request
from models import Post, db

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
    post_id = Post.query.get_or_404(post_id)
    user_id = Post.query.get_or_404(user_id)
    title = request.form.get('post_title', '')
    caption = request.form.get('post_content', '')
    song = request.form.get('song_select', '')
    create = request.form.get('create', '') #???
    cancel = request.form.get('cancel', '') #???

    if title == '' or song == '' or caption == '':
        abort(400)

    new_post = Post(title=title, song=song)
    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/profile/{new_post.post_id}')   

@router.get('/<post_id>/edit') #TODO:edit parts of the title
def get_edit_Post_form(post_id):
    post_to_edit = Post.query.get_or_404(post_id)
    return render_template('editpost.html', post = post_to_edit)     

@router.post('/<post_id>') #TODO: do the updating for the post
def update_post(post_id):
    post_to_update = Post.query.get_or_404(post_id)
    user_id = Post.query.get_or_404(user_id)
    title = request.form.get('Title', '')
    caption = request.form.get('Caption', '')
    song = request.form.get('song_select',  '')
    create = request.form.get('create', '') #???
    cancel = request.form.get('cancel', '') #???

    if title == '' or song == '' or caption == '':
        abort(400)

    post_to_update.title = title
    post_to_update.caption = caption
    post_to_update.song = song

    db.session.commit()

    return redirect(f'/profile/{post_id}')

@router.post('/<post_id>/delete') #TODO: delete a post
def delete_post(post_id):
    post_to_delete = Post.query.get_or_404(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect('/profile')
