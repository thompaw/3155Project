# Implement all CRUD elements
# Reference this: https://github.com/jacobtie/itsc-3155-module-10-demo/blob/main/blueprints/book_blueprint.py
from flask import Blueprint, abort, redirect, render_template, request
from models import User_Profile, db

router = Blueprint('user_profile_router', __name__, url_prefix='/user_profile')

@router.get('')
def get_all_user_profile():
    pass

@router.get('/<user_id>')
def get_single_user_profile(user_id):
    pass

@router.get('/new')
def create_user_profile_form():
    pass

@router.post('')
def create_user_profile():
    pass

@router.get('/<user_id>/edit')
def get_edit_user_profile_form(user_id):
    pass

@router.post('/<user_id>')
def update_user_profile(user_id):
    pass

@router.post('/<user_id>/delete')
def delete_user_profile(user_id):
    pass