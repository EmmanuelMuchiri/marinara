from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import UpdateProfile
from ..models import User
from flask_login import login_required,current_user
from .. import db,photos
import markdown2  

@main.route('/')
def index():
    '''
    view root page function that returns index page
    '''
    title = 'Home'
    return render_template('index.html', title = title)


