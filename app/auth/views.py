from . import auth
from .forms import RegistrationForm,LoginForm
from flask_login import login_user,logout_user,login_required,current_user
from ..models import User
from flask import redirect,render_template,url_for,flash
from .. import db







@auth.route('/register', methods = ['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username =form.username.data, email = form.email.data)
        user.set_password(form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('registration.html', form=form)