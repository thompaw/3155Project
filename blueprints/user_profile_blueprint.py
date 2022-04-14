# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
from flask import Blueprint, abort, redirect, render_template, request
from models import userprofile, db

router = Blueprint('user_profile_router', __name__, url_prefix='/user_profile')

# Hirdhay
@router.get('')
def get_all_user_profile():
    all_users = userprofile.query.all()
    return render_template('all_users.html', users = all_users)

# Haley
@router.get('/<user_id>')
def get_single_user_profile(user_id):
    single_user_profile = userprofile.query.get_or_404(user_id)
    return render_template('single_user_profile.html', user_profile = single_user_profile)

# Haley
@router.get('/new')
def create_user_profile_form():
    return render_template('signup.html')

# Haley
@router.post('')
def create_user_profile():
    name = request.form.get('first-name', '') + " " + request.form.get('last-name', '')
    email = request.form.get('email', '')
    password = request.form.get('password', '')

    if name == '' or email == '' or password == '':
        abort(400)

    new_user_profile = userprofile(name=name, email=email, password=password)
    db.session.add()
    db.session.commit()

    return(f'/user_profile/{new_user_profile.user_id}')

# Hirdhay
@router.get('/<user_id>/edit')
def get_edit_user_profile_form(user_id):
    pass

# Hirdhay
@router.post('/<user_id>')
def update_user_profile(user_id):
    pass

# Hirdhay
@router.post('/<user_id>/delete')
def delete_user_profile(user_id):
    pass
