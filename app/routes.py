from app import app, db, mail, Message
from flask import render_template, request, flash, redirect, url_for
from app.forms import UserInfoForm, LoginForm
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash


@app.route('/')
@app.route('/index')
def index():
    user ={'username': 'Kateri'}
    return render_template('index.html', title='Home', user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = "The Phonebook | REGISTER"
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        phone - form.phone.data
        password = form.password.data
        # print(username, email, phone, password)
        
        # create a new instance of User
        new_user = User(username, email, phone, password)
        # add new instance to our database
        db.session.add(new_user)
        # commit database
        db.session.commit()

        # Send email to new user
        msg = Message(f'Welcome, {username}', [email])
        msg.body = "Thank you for joining the phonebook. I hope to keep in touch!"
        msg.html = "<p>Thanks for joining the phone. Let's be in touch soon!</p>"

        mail.send(msg)

        flash("You have succesfully signed up!", "success")
        return redirect(url_for('index'))
    return render_template('register.html', title=title, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "The Phonebook| LOGIN"
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            flash("Incorrect Email/Password. Please try again", 'danger')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        flash("You have successfully logged in!", 'success')
        next_page = request.args.get('next')
        if next_page:
            return redirect(url_for(next_page.lstrip('/')))
        return redirect(url_for('index'))

    return render_template('login.html', title=title, form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("You have succesfully logged out", 'primary')
    return redirect(url_for('index'))

@app.route('/update', methods=['GET', 'POST'])
def update():

    return render_template('update.html', title=title, form=form)

