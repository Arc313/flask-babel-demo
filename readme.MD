# Flask-Babel Demo

## Setup Instructions
1. Run `pip install -r requirements.txt`.
2. Run `serve.bat`.
3. Go to <http://localhost:5000>.

## Flask Babel Instructions
1. Create a babel.cfg file as shown in the project directory.
2. Use `gettext` and `ngettext` (latter one for plural text) for strings requiring translations.
3. Run `pybabel extract -F babel.cfg -i messages.pot .`
4. Run `pybabel init -i messages.pot -d translations -l mr` (mr stands for Marathi).
5. Open the `translations\mr\LC_MESSAGES\messages.po` file and fill in the translations.
6. Run `pybabel compile -d translations` to compile all translations.
7. Run your application.