from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import PasswordVault
from myapp.password_posts.forms import PasswordPostForm

password_posts = Blueprint('password_posts', __name__)

@password_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PasswordPostForm()
    if form.validate_on_submit():
        password_post = PasswordVault(title=form.title.data, text=form.text.data, user_id=current_user.id)
        db.session.add(password_post)
        db.session.commit()
        flash('Password Post was Created')
        print('Password Post was created')
        return redirect(url_for('core.index'))
    return render_template('create_password_post.html', form=form)

# Make sure the password_post_id is an integer!

@password_posts.route('/<int:password_post_id>')
def password_post(password_post_id):
    password_post = PasswordVault.query.get_or_404(password_post_id) 
    return render_template('password_post.html', title=password_post.title, date=password_post.date, post=password_post)