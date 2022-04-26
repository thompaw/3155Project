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
    postnum = None
    usernum = None
    goop = request.form.get('content', '')

    new_comment = Comment(user_id=usernum, post_id=postnum, content=goop)
    db.session.add(new_comment)
    db.session.commit()

    return redirect(f'Comment/<comment_id>')

# READ
@router.get('')  # per post
def get_all_comments(post_id):
    pass

@router.get('/<comment_id>')  # single comment
def get_single_comment(comment_id):
    pass

# UPDATE
@router.post('/<comment_id>')
def update_comment(comment_id):
    updating_comment = Comment.query.get_or_404(comment_id)

    goop = request.form.get('content', '')

    if len(goop) < 1:
        abort(400)

    updating_comment.content = goop

    db.session.commit()

    return redirect(f'Comment/<comment_id>')

# DELETE
@router.post('/<comment_id>/delete')
def delete_comment(comment_id):
    comment_to_delete = Comment.query.get_or_404(comment_id)
    db.session.delete(comment_to_delete)
    db.session.commit()
    return redirect('/<post_id>')
