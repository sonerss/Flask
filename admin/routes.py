from flask import Blueprint,render_template

admin = Blueprint('admin', __name__,static_folder='static',template_folder='pages')

@admin.route('/')
def home():
    return render_template('admin/index.html')