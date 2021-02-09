from flask import Flask, request, render_template, session, redirect, url_for
from flask_babel import Babel, gettext

app = Flask(__name__)
app.config['SECRET_KEY'] = 'notasecret'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # if a user is logged in, use the locale from the user settings
    if 'language' in session:
        return session['language']
    # otherwise try to guess the language from the user accept
    # header the browser transmits.  We support en/mr in this
    # example. The best match wins.
    return request.accept_languages.best_match(['en', 'mr'])

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/answer', methods=['GET'])
def answer():
    return gettext(u'The answer to 2 + 2 is 4!')

@app.route('/switch', methods=['POST'])
def switch():
    if 'language' in session and session['language'] == 'mr':
        session['language'] = 'en'
    else:
        session['language'] = 'mr'
    
    return redirect(url_for('home'))
