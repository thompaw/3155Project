# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
from flask import Blueprint, abort, redirect, render_template, request, session
from models import Userprofile, db

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

    single_user_profile = Userprofile.query.get_or_404(user_id)
    
    return render_template('single_user_profile.html', user = single_user_profile, user_in_session = session['user']['user_id'])

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
    print(user_id)

    db.session.delete(user_to_endit)

    db.session.commit()

     # delete the user session
    del session['user']

    # redirect to landing page
    return redirect('/')
