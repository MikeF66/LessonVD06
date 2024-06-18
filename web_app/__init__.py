from flask import Flask


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'web_app/static/uploads/'
# web_app.config['SECRET_KEY'] = 'you_will_never_guess'


from web_app import routes
