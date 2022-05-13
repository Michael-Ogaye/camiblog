from . import auth
from .forms import RegistrationForm,LoginForm
from flask_login import login_user,logout_user,login_required,current_user
from ..models import User
from flask import redirect,render_template,url_for,flash,request
from .. import db







@auth.route('/register', methods = ['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username =form.username.data, email = form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('main.index'))
        flash('Invalid email address or Password.')    
    return render_template('auth/login.html', form=form)
