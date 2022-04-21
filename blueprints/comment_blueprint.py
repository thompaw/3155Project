# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
from flask import Blueprint, abort, redirect, render_template, request
from models import db, Comment

# router definition
router = Blueprint('Comment_router', __name__, url_prefix='/Comment')

# CREATE
@router.get('/new_comment')
def create_user_profile_form():
    return render_template('signup.html')

@router.post('')
def create_comment():
    pass

# READ
@router.get('')  # per post

@router.get('')  # single comment

# UPDATE
@router.post('/<comment_id>')
def update_comment(comment_id):
    book_to_update = Book.query.get_or_404(book_id)
    author = request.form.get('author', '')
    rating = request.form.get('rating', 0, type=int)

    if author == '' or rating < 1 or rating > 5:
        abort(400)

    book_to_update.author = author
    book_to_update.rating = rating

    db.session.commit()

    return redirect(f'/books/{book_id}')

# DELETE
@router.post('/<comment_id>/delete')
def delete_comment(comment_id):
    comment_to_delete = Comment.query.get_or_404(comment_id)
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect('/<post_id>')
