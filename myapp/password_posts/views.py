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
    return render_template('create_post.html', form=form)

# Make sure the password_post_id is an integer!

@password_posts.route('/<int:password_post_id>')
def password_post(password_post_id):
    password_post = PasswordVault.query.get_or_404(password_post_id) 
    return render_template('password_post.html', title=password_post.title, date=password_post.date, post=password_post)

@password_posts.route('/<int:password_post_id>/update',methods=['GET','POST'])
@login_required
def update(password_post_id):
    password_post = PasswordVault.query.get_or_404(password_post_id)

    if password_post.author != current_user:
        abort(403)

    form = PasswordPostForm()

    if form.validate_on_submit():
        password_post.title = form.title.data
        password_post.text = form.text.data
        db.session.commit()
        flash('password Post Updated')
        return redirect(url_for('password_posts.password_post',password_post_id=password_post.id))

    elif request.method == 'GET':
        form.title.data = password_post.title
        form.text.data = password_post.text

    return render_template('create_post.html',title='Updating',form=form)


@password_posts.route('/<int:password_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(password_post_id):

    password_post = PasswordVault.query.get_or_404(password_post_id)
    if password_post.author != current_user:
        abort(403)

    db.session.delete(password_post)
    db.session.commit()
    flash('password Post Deleted')
    return redirect(url_for('core.index'))