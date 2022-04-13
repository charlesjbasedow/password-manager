from flask import render_template, request, Blueprint
from myapp.models import PasswordVault

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    password_posts = PasswordVault.query.order_by(PasswordVault.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', password_posts=password_posts)

@core.route('/info')
def info():
    return render_template('info.html')