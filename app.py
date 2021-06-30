from flask import Flask, render_template, redirect, flash, url_for, session, request, logging, g
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
import sqlite3
from minut import zestaw_par, term, wyniki, date, pause, club, games, points, goals
from next_game import last, next_game
from lnp import game, tjm, tr, tablejs, tablejm, tabletr, celuloza19, celulozajm, celulozatr
# from next_lzpn import next_game
import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret123'

DATABASE = 'news.db'

last = last()
next_game = next_game()
clubs = zestaw_par()
terms = term()
wynik = wyniki()
kolejka = date()
pauza = pause()
klub = club()
mecze = games()
punkty = points()
bramki = goals()
game = game()
tjm = tjm()
tr = tr()
teams = tablejs()
punktyjs = teams[0]
teamsjs = teams[1]
teamsjm = tablejm()
punktyjm = teamsjm[0]
teamjm = teamsjm[1]
teamstr = tabletr()
punktytr = teamstr[0]
teamtr = teamstr[1]
celuloza19 = celuloza19()
celulozajm = celulozajm()
celulozatr = celulozatr()

term()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def gry():
    cur = get_db()
    result = cur.execute("SELECT * FROM NextGame ORDER BY id DESC")
    gry = result.fetchall()
    return gry


@app.context_processor
def inject_user():
    games = gry()
    return dict(last=last, next_game=next_game, games=games)


@app.route("/")  # articles = news()
def news():
    date_now = datetime.datetime.now()

    celulozang19 = []
    for g in celuloza19:
        date = g[0]
        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozang19.append(g)

    try:
        next_rival19 = sorted(celulozang19, key=lambda x: x[0])
        celuloza19ng = next_rival19[0]
    except:
        celuloza19ng = ['-', '-', '-', '-', '-']

    celulozangjm = []
    for g in celulozajm:
        date = g[0]
        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozangjm.append(g)

    try:
        next_rivaljm = sorted(celulozangjm, key=lambda x: x[0])
        next_gamejm = next_rivaljm[0]

    except:
        next_gamejm = ['-', '-', '-', '-', '-']

    celulozangtr = []
    for g in celulozatr:
        date = g[0]
        # print(date)
        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozangtr.append(g)

    try:
        next_rival = sorted(celulozangtr, key=lambda x: x[0])
        next_gametr = next_rival[0]
    except:
        next_gametr = ['-', '-', '-', '-', '-']

    js = celuloza19ng
    jm = next_gamejm
    tr = next_gametr
    sen = next_game
    date_now = datetime.datetime.now()
    datesen = sen[2]
    datejs = js[0]
    datejm = jm[0]
    datetr = tr[0]
    if datesen != '-' and datesen.year == date_now.year and datesen.month == date_now.month and datesen.day == date_now.day:
        senng = True
    else:
        senng = False
    if datejs != '-' and datejs.year == date_now.year and datejs.month == date_now.month and datejs.day == date_now.day:
        jsng = True
    else:
        jsng = False
    if datejm != '-' and datejm.year == date_now.year and datejm.month == date_now.month and datejm.day == date_now.day:
        jmng = True
    else:
        jmng = False
    if datetr != '-' and datetr.year == date_now.year and datetr.month == date_now.month and datetr.day == date_now.day:
        trng = True
    else:
        trng = False

    games = gry()

    next_bool = [senng, jsng, jmng, trng]

    # Create cursor
    cur = get_db()

    # get articles
    result = cur.execute("SELECT * FROM articles ORDER BY id DESC")

    articles = result.fetchall()

    if result is None:
        msg = "nie znaleziono artykułów"
        return render_template('news.html', msg=msg)

    else:
        return render_template('news.html', articles=articles, next_bool=next_bool, next_game=next_game,
                               celuloza19ng=celuloza19ng, next_gamejm=next_gamejm, next_gametr=next_gametr,
                               senng=senng, jsng=jsng, jmng=jmng, trng=trng, games=games)

    # close connection
    cur.close()


@app.route("/admin")
def admin():
    return render_template('admin.html')


# Artykuły
@app.route("/articles")
def home():
    date_now = datetime.datetime.now()

    celulozang19 = []
    for g in celuloza19:
        date = g[0]
        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozang19.append(g)

    try:
        next_rival19 = sorted(celulozang19, key=lambda x: x[0])
        celuloza19ng = next_rival19[0]
    except:
        celuloza19ng = ['-', '-', '-', '-', '-']

    celulozangjm = []
    for g in celulozajm:
        date = g[0]
        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozangjm.append(g)

    try:
        next_rivaljm = sorted(celulozangjm, key=lambda x: x[0])
        next_gamejm = next_rivaljm[0]

    except:
        next_gamejm = ['-', '-', '-', '-', '-']

    celulozangtr = []
    for g in celulozatr:
        date = g[0]
        # print(date)
        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozangtr.append(g)

    try:
        next_rival = sorted(celulozangtr, key=lambda x: x[0])
        next_gametr = next_rival[0]
    except:
        next_gametr = ['-', '-', '-', '-', '-']


    js = celuloza19ng
    jm = next_gamejm
    tr = next_gametr
    sen = next_game
    date_now = datetime.datetime.now()
    datesen = sen[2]
    datejs = js[0]
    datejm = jm[0]
    datetr = tr[0]
    if datesen.year == date_now.year and datesen.month == date_now.month and datesen.day == date_now.day:
        senng = True
    else:
        senng = False
    if datejs != '-' and datejs.year == date_now.year and datejs.month == date_now.month and datejs.day == date_now.day:
        jsng = True
    else:
        jsng = False
    if datejm != '-' and datejm.year == date_now.year and datejm.month == date_now.month and datejm.day == date_now.day:
        jmng = True
    else:
        jmng = False
    if datetr != '-' and datetr.year == date_now.year and datetr.month == date_now.month and datetr.day == date_now.day:
        trng = True
    else:
        trng = False

    games = gry()

    next_bool = [senng, jsng, jmng, trng]

    # Create cursor
    cur = get_db()

    # get articles
    result = cur.execute("SELECT * FROM articles ORDER BY id DESC")

    articles = result.fetchall()

    if result is None:
        msg = "nie znaleziono artykułów"
        return render_template('news.html', msg=msg)

    else:
        return render_template('news.html', articles=articles, next_bool=next_bool, next_game=next_game,
                               celuloza19ng=celuloza19ng, next_gamejm=next_gamejm, next_gametr=next_gametr, senng=senng,
                               jsng=jsng, jmng=jmng, trng=trng, games=games)

    # close connection
    cur.close()


# Pojedynczy atykuł


@app.route("/articles/<string:id>/")
def article(id):
    # Create cursor
    cur = get_db()

    # get article
    result = cur.execute("SELECT * FROM articles WHERE id = ?", [id])

    article = result.fetchone()

    return render_template('article.html', article=article)

    # close connection
    cur.close()


@app.route("/board")
def board():
    return render_template('zarzad.html')


@app.route("/coaches")
def coaches():
    return render_template('trenerzy.html')


@app.route("/contact")
def contact():
    return render_template('kontakt.html')


@app.route("/history")
def history():
    return render_template('historia.html')


@app.route("/juniorm")
def juniorm():
    date_now = datetime.datetime.now()

    celulozang = []
    for g in celulozajm:
        date = g[0]

        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozang.append(g)

    next_rival = sorted(celulozang, key=lambda x: x[0])

    try:
        next_gamejm = next_rival[0]
    except:
        next_gamejm = ['-', '-', '-', '-', '-']

    return render_template('juniorm.html', next_gamejm=next_gamejm)


@app.route("/juniors")
def juniors():
    date_now = datetime.datetime.now()

    celulozang = []
    for g in celuloza19:
        date = g[0]
        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozang.append(g)

    try:
        next_games = [elem for elem in celulozang if elem[0]]
        next_rival = sorted(next_games, key=lambda x: x[0])
        celuloza19ng = next_rival[0]

    except:
        celuloza19ng = ['-', '-', '-', '-', '-']

    return render_template('juniors.html', celuloza19ng=celuloza19ng)


@app.route("/loop")
def loop():
    # Create cursor
    cur = get_db()

    # get article
    result = cur.execute("SELECT number FROM Loop WHERE id = 1")

    number = result.fetchone()
    return render_template('loop.html', number=number)
    cur.close()


@app.route("/schedule")
def schedule():
    return render_template('terminarz.html', clubs=clubs, terms=terms, wynik=wynik, kolejka=kolejka, pauza=pauza,
                           last=last)


@app.route("/schedulejm")
def schedulejm():
    date_now = datetime.datetime.now()

    celulozang = []
    for g in celulozajm:
        date = g[0]

        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozang.append(g)

    next_rival = sorted(celulozang, key=lambda x: x[0])

    try:
        next_gamejm = next_rival[0]
    except:
        next_gamejm = ['-', '-', '-', '-', '-']

    return render_template('terminarzjm.html', tjm=tjm, next_gamejm=next_gamejm)


@app.route("/schedulejs")
def schedulejs():
    date_now = datetime.datetime.now()

    celulozang = []
    for g in celuloza19:
        date = g[0]
        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozang.append(g)

    next_rival = sorted(celulozang, key=lambda x: x[0])

    try:
        celuloza19ng = next_rival[0]
    except:
        celuloza19ng = ['-', '-', '-', '-', '-']

    return render_template('terminarzjs.html', game=game, celuloza19ng=celuloza19ng)


@app.route("/scheduletr")
def scheduletr():
    date_now = datetime.datetime.now()

    celulozang = []
    for g in celulozatr:
        date = g[0]
        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozang.append(g)


    next_rival = sorted(celulozang, key=lambda x: x[0])

    try:
        next_gametr = next_rival[0]
    except:
        next_gametr = ['-', '-', '-', '-', '-']

    return render_template('terminarztr.html', tr=tr, next_gametr=next_gametr)


@app.route("/sponsors")
def sponsors():
    sponsors = True
    return render_template('sponsorzy.html', sponsors=sponsors)


@app.route("/table")
def table():
    return render_template('tabela.html', klub=klub, mecze=mecze, punkty=punkty, bramki=bramki)


@app.route("/tablejm")
def tabelajm():
    return render_template('tabelajm.html', punktyjm=punktyjm, teamjm=teamjm)


@app.route("/tablejs")
def tabelajs():
    return render_template('tabelajs.html', punktyjs=punktyjs, teamsjs=teamsjs)


@app.route("/tabletr")
def tabelatr():
    return render_template('tabelatr.html', punktytr=punktytr, teamtr=teamtr)


@app.route("/team")
def team():
    return render_template('kadra.html')


@app.route("/tramp")
def tramp():
    date_now = datetime.datetime.now()

    celulozang = []
    for g in celulozatr:
        date = g[0]
        if date > date_now:
            g = [date, g[1], g[2], g[3], g[4]]
            celulozang.append(g)

    next_rival = sorted(celulozang, key=lambda x: x[0])

    try:
        next_gametr = next_rival[0]
    except:
        next_gametr = ['-', '-', '-', '-', '-']

    return render_template('trampkarz.html', next_gametr=next_gametr)


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
        cur = get_db()

        cur.execute(
            "INSERT INTO users (name, email, username, password) VALUES (?,?,?,?)", (name, email, username, password))

        # cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",
        #             (name, email, username, password))

        # commit to DB
        cur.commit()

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
        cur = get_db()

        # Get user by username
        result = cur.execute(
            "SELECT * FROM users WHERE username = ?", [username])

        result = result.fetchall()

        if result:
            # Get stored hash
            data = result
            password = data[0][4]
            # password = data['password']

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
    # Create cursor
    cur = get_db()

    # get articles
    result = cur.execute("SELECT * FROM articles ORDER BY id DESC")

    articles = result.fetchall()
    print(articles)

    if result is None:
        msg = "nie znaleziono artykułów"
        return render_template('dashboard.html', msg=msg)
    else:
        return render_template('dashboard.html', articles=articles)

    # close connection
    cur.close()


# Formularz artykułu


class ArticleForm(Form):
    title = StringField('Tytuł', [validators.Length(min=1, max=200)])
    body = TextAreaField('Treść', [validators.Length(min=30)])


@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        # kursor
        cur = get_db()

        # execute
        cur.execute("INSERT INTO articles (title, body, author) VALUES (?, ?, ?)",
                    (title, body, session['username']))

        # commit
        cur.commit()

        # close
        cur.close()

        flash('Artykuł dodany', 'success')

        return redirect(url_for('dashboard'))

    return render_template('add_article.html', form=form)


# edit article


@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    # Create cursor
    cur = get_db()

    # Get article by id
    result = cur.execute("SELECT * FROM articles WHERE id = ?", [id])

    article = result.fetchone()
    # cur.close()

    # Get form
    form = ArticleForm(request.form)

    # Populate article form fields
    form.title.data = article[1]
    form.body.data = article[3]

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        # kursor
        cur = get_db()

        # execute
        cur.execute(
            "UPDATE articles SET title=?, body=? WHERE id = ?", (title, body, id))

        # commit
        cur.commit()

        # close
        cur.close()

        flash('Artykuł został zaktualizowany', 'success')

        return redirect(url_for('dashboard'))

    return render_template('edit_article.html', form=form)


# Delete article
@app.route('/delete_article/<string:id>', methods=["POST"])
@is_logged_in
def delete_article(id):
    # Create cursor
    cur = get_db()

    # Execute
    cur.execute("DELETE FROM articles WHERE id = ?", [id])

    # commit
    cur.commit()

    # close
    cur.close()

    flash('News został usunięty', 'success')

    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(host='0.0.0.0')  # host='0.0.0.0'
