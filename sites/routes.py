from flask import Blueprint,render_template

sites = Blueprint('sites', __name__,static_folder='static',template_folder='pages')

@sites.route('/')
def home():
    return render_template('sites/index.html')