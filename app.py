from flask import Flask, render_template, redirect, flash, url_for, session, request, logging
from data import news
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)


# Config MySQL
app.config['MYSQL_HOST'] = 'serwer1926689.home.pl'
app.config['MYSQL_USER'] = '31624366_celuloza'
app.config['MYSQL_PASSWORD'] = 'Celuloza2020'
app.config['MYSQL_DB'] = '31624366_celuloza'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = 'secret123'
# init MYSQL
mysql = MySQL(app)


articles = news()


@app.route("/")
def news():
    return render_template('home.html')

# Artykuły


@app.route("/articles")
def home():
    return render_template('news.html', articles=articles)

# Pojedynczy atykuł


@app.route("/articles/<string:id>/")
def article(id):
    return render_template('article.html', id=id)


@app.route("/history")
def history():
    return render_template('historia.html')


@app.route("/board")
def board():
    return render_template('zarzad.html')


@app.route("/team")
def team():
    return render_template('kadra.html')


@app.route("/schedule")
def schedule():
    return render_template('terminarz.html')


@app.route("/table")
def table():
    return render_template('tabela.html')


@app.route("/juniors")
def juniors():
    return render_template('juniors.html')


@app.route("/juniorm")
def juniorm():
    return render_template('juniorm.html')


@app.route("/tramp")
def tramp():
    return render_template('trampkarz.html')


@app.route("/uks")
def uks():
    return render_template('uks.html')

# Formularz rejestracji


class RegisterForm(Form):
    name = StringField('Imię', [validators.Length(min=1, max=50)])
    username = StringField('Nick', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Hasło', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not march')
    ])
    confirm = PasswordField('Confirm Password')


# Rejestracja


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))

        # create cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",
                    (name, email, username, password))

        # commit to DB
        mysql.connection.commit()

        # close connection
        cur.close()

        flash('Zostałeś zarejestrowany i możesz się zalogować', 'success')

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# User login


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get from fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute(
            "SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # compare passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('Jesteś zalogowany', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Niepoprawne dane logowania'
                return render_template('login.html', error=error)

            # Close connection
            cur.close()
        else:
            error = 'Użytkownik nie znaleziony'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user logged in


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Proszę się zalogować', 'danger')
            return redirect(url_for('login'))
    return wrap

# Wylogowanie


@app.route('/logout')
def logout():
    session.clear()
    flash('Zostałeś wylogowany', 'success')
    return redirect(url_for('login'))


# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run()
