from flask import Flask
import config
from admin.routes import admin
from sites.routes import sites

app = Flask(__name__)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(sites,url_prefix='/sites')


@app.route('/')
def test():
    return 'main page'

if __name__ == '__main__':
    app.secret_key = config.BaseConfig.SECRET_KEY
    app.run(debug=True)

