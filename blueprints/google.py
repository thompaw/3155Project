from flask import Blueprint, abort, redirect, render_template, request, session
from models import Userprofile, db
googleData = []

router = Blueprint('google_router', __name__, url_prefix='/google')

@router.post('/in') 
def inp():
    googleData.clear()
    googleData.append(request.json)

    print(googleData[0]['googleIdToken'])
    email = googleData[0]['googleIdToken']
    #googleData = json.loads(googleData)
    #print("here" + googleData[0]['googleIdToken'])

    # result = Userprofile.query.filter(Userprofile.user_email.has(username=googleData[0]['googleIdToken']))
    googleUser = Userprofile.query.filter_by(user_email=email).first()

    # If a returning user start a session
    if googleUser is not None:
        session['user'] = {
            'username': googleUser.user_name,
            'user_id': googleUser.user_id,
        }
        return '1'
        

    # Make a user with given email
    else:
        return '0'


@router.get('/signup')
def signedin():
    #print(googleData[0]['googleIdToken'])

    return render_template('signup_google.html', email=googleData[0]['googleIdToken'])
