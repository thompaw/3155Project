# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
import string
from xmlrpc.client import boolean
from flask import Blueprint, abort, redirect, render_template, request
from models import Post, db

# database connection stuffs below
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/Project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# placeholder lists of dictionaries till sql implementation

router = Blueprint('Post_router', __name__, url_prefix='/Post')

@router.post('')
def create_post():
    post_id = post.query.get_or_404(post_id)
    user = post.query.get_or_404(user_id)
    title = request.form.get('Title', type=string)
    caption = request.form.get('Caption', type=string)
    song = request.form.get('song_select', type=string)
    create = request.form.get('Create', type=boolean)
    cancel = request.form.get('cancel', type=boolean)

    if title == '' or song == '' or caption == '':
        abort(400)

    new_post = Post(title=title, title=title, song=song)
    db.session.add(new_post)
    db.session.commit()

    return redirect(f'/profile/{new_post.post_id}')

@router.get('/<post_id>/edit')
def get_edit_post_form(post_id):
    post_to_edit = post.query.get_or_404(post_id)
    return render_template('edit_post_form.html', post=post_to_edit)

@router.post('/<post_id>')
def update_post(post_id):
    post_to_update = post.query.get_or_404(post_id)
    user = post.query.get_or_404(user_id)
    title = request.form.get('Title', type=string)
    caption = request.form.get('Caption', type=string)
    song = request.form.get('song_select', type=string)
    create = request.form.get('Create', type=boolean)
    cancel = request.form.get('cancel', type=boolean)

    if title == '' or song == '' or caption == '':
        abort(400)

    post_to_update.title = title
    post_to_update.caption = cation
    post_to_update.song = song
    

    db.session.commit()

    return redirect(f'/profile/{post_id}')


@router.post('/<post_id>/delete')
def delete_post(post_id):
    post_to_delete = post.query.get_or_404(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect('/profile')
