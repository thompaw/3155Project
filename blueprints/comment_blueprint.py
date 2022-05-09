# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
from flask import Blueprint, abort, redirect, render_template, request, session
from models import db, Comment

# router definition
router = Blueprint('Comment_router', __name__, url_prefix='/comment')

# CREATE
@router.get('/new_comment')
def create_user_profile_form():
    return render_template('signup.html')  # return the user with the new comment form

@router.post('')
def create_comment():  # taking data from the form
    postId = request.form.get('postId', '')
    usernum = session['user']['user_id']  # should auto grab these based on where the form is located
    comment = request.form.get('comment', '')
    new_comment = Comment(user_id=usernum, post_id=postId, content=comment)  # create a new comment object using the data from the form
    db.session.add(new_comment)
    db.session.commit()  # save changes and commit to db

    return redirect(f'post/{postId}')  # send user to their new comment

# READ
# @router.get('/<post_id>')  # per post
# def get_comments_per_post(post_id):  # grab all comments associated to a single post
#     comment_list = Comment.query.filter_by(post_id=post_id).all()

#     return render_template('single_post.html', post=post_id, comments=comment_list)  # needs work


# @router.get('/<comment_id>')  # single comment
# def get_single_comment(comment_id):  # grab a single comment by it's id
#     single_comment = Comment.query.get_or_404(comment_id).first()
#     return render_template('comments/<comment_id>', comment=single_comment)

# UPDATE
@router.post('/<comment_id>')
def update_comment(comment_id):
    updating_comment = Comment.query.get_or_404(comment_id)  # get the object to be updated

    goop = request.form.get('content', '')  # get the new content from the edit form, yet to be implemented

    if goop == '':  # if the content of the comment is empty, don't accept it
        abort(400)

    updating_comment.content = goop  # change the old to the new

    db.session.commit()  # commit changes to the db

    return redirect(f'comment/<comment_id>') # send the user to their new comment

# DELETE
@router.post('/<comment_id>/delete')
def delete_comment(comment_id):
    comment_to_delete = Comment.query.get_or_404(comment_id)  # grab the comment id 
    db.session.delete(comment_to_delete)  # delete the comment and then save changes. 
    db.session.commit()
    return redirect('/<post_id>')  # return to the post that comment was on
