# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
from flask import Blueprint, abort, redirect, render_template, request, session
from models import Comment, Follower, Post, Userprofile, db

router = Blueprint('user_profile_router', __name__, url_prefix='/user_profile')

# Hirdhay
@router.get('')
def get_all_user_profile():
    # if the user is not logged in it aborts to 401
    if not 'user' in session:
        abort(401)

    all_users = Userprofile.query.all()
    return render_template('all_users.html', users = all_users, user_in_session = session['user']['user_id'])

# Haley
@router.get('/<user_id>')
def get_single_user_profile(user_id):
    # if the user is not logged in it aborts to 401
    if not 'user' in session:
        abort(401)
    followercount = Follower.query.filter_by(following_id=user_id).count()
    single_user_profile = Userprofile.query.get_or_404(user_id)
    
    isFollowing = False
    x = Follower.query.filter_by(follower_id=session['user']['user_id'], following_id=user_id).first()
    print(x)
    if x is not None:
        isFollowing = True
    
    return render_template('single_user_profile.html', user = single_user_profile, user_in_session = session['user']['user_id'], followercount = followercount, isFollowing = isFollowing)

# Hirdhay
@router.get('/<user_id>/edit')
def get_edit_user_profile_form(user_id):
    user_to_edit = Userprofile.query.get_or_404(user_id)
    return render_template('editprofile.html', user = user_to_edit, user_in_session = session['user']['user_id'])

# Hirdhay
@router.post('/<user_id>')
def update_user_profile(user_id):
    user_to_update = Userprofile.query.get_or_404(user_id)
    name = request.form.get('name', '')
    location = request.form.get('location', '')
    biography = request.form.get('biography', '')

    if location == '' or biography == '':
        abort(400)


    user_to_update.user_location = location
    user_to_update.user_biography = biography

    db.session.commit()

    #return redirect(f'/user_profile/{user_id}', user_in_session = session['user']['user_id'])
    return redirect(f'/user_profile/{user_id}')
    
# Hirdhay
@router.post('/<user_id>/delete')
def delete_user_profile(user_id):
    print("here" + user_id)
    user_to_endit = Userprofile.query.get_or_404(user_id)

    #must delete all posts made by user and all comments related to post made by said user
    posts_to_delete = Post.query.filter_by(user_id=user_to_endit.user_id).all() 
    for post in posts_to_delete: #you have to delete all comments related to that post before deleting the post
        comments_to_delete = Comment.query.filter_by(post_id=post.post_id).all()
        for comment in comments_to_delete: #you have to delete all comments related to that post before deleting the post
            db.session.delete(comment)
        db.session.delete(post)
    
    comments_by_user = Comment.query.filter_by(user_id=user_to_endit.user_id).all()

    #have to delete all comments made by said user
    for comment in comments_by_user:
        db.session.delete(comment)

    #sign user out
    if 'user' not in session:
        abort(401)

    # delete the user session
    del session['user']
    #finally delete user
    db.session.delete(user_to_endit)
    db.session.commit()
    return redirect('/')

@router.post('/<user_id>/follow')
def follow_user(user_id):
    follower_id = session['user']['user_id']
    following_id = user_id

    already = Follower.query.filter_by(follower_id=follower_id, following_id=following_id).first()
    print(already)


    if already is not None:
        db.session.delete(already)
    else:
        new = Follower(follower_id=follower_id, following_id=following_id)
        db.session.add(new)

    db.session.commit()


    return redirect(f'/user_profile/{user_id}')

