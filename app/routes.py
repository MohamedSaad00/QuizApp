from app import app
from flask import render_template, request, redirect, url_for, session, g, flash
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm, QuestionForm
from app.models import User, Questions
from app import db


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        g.user = user

# --- Auto-populate questions if table is empty ---
from app.models import Questions
from app import db, app

with app.app_context():
    if Questions.query.count() == 0:
        questions = [
            Questions(ques="What is the capital of France?", a="Paris", b="London", c="Berlin", d="Madrid", ans="Paris"),
            Questions(ques="Which planet is known as the Red Planet?", a="Earth", b="Mars", c="Jupiter", d="Saturn", ans="Mars"),
            Questions(ques="Who wrote 'Romeo and Juliet'?", a="Charles Dickens", b="William Shakespeare", c="Jane Austen", d="Mark Twain", ans="William Shakespeare"),
            Questions(ques="What is the largest ocean on Earth?", a="Atlantic Ocean", b="Indian Ocean", c="Arctic Ocean", d="Pacific Ocean", ans="Pacific Ocean"),
            Questions(ques="What is the chemical symbol for water?", a="O2", b="H2O", c="CO2", d="NaCl", ans="H2O"),
            Questions(ques="How many continents are there?", a="5", b="6", c="7", d="8", ans="7"),
            Questions(ques="What is the fastest land animal?", a="Lion", b="Cheetah", c="Tiger", d="Leopard", ans="Cheetah"),
            Questions(ques="Who painted the Mona Lisa?", a="Vincent Van Gogh", b="Pablo Picasso", c="Leonardo da Vinci", d="Claude Monet", ans="Leonardo da Vinci"),
            Questions(ques="What is the hardest natural substance?", a="Gold", b="Iron", c="Diamond", d="Silver", ans="Diamond"),
            Questions(ques="Which language is the most spoken worldwide?", a="English", b="Mandarin Chinese", c="Spanish", d="Hindi", ans="Mandarin Chinese"),
            Questions(ques="What is the smallest prime number?", a="0", b="1", c="2", d="3", ans="2"),
            Questions(ques="Which country is known as the Land of the Rising Sun?", a="China", b="Japan", c="Thailand", d="South Korea", ans="Japan"),
            Questions(ques="What is the boiling point of water?", a="90°C", b="100°C", c="110°C", d="120°C", ans="100°C"),
            Questions(ques="Who discovered gravity?", a="Albert Einstein", b="Isaac Newton", c="Galileo Galilei", d="Nikola Tesla", ans="Isaac Newton"),
            Questions(ques="What is the largest mammal?", a="Elephant", b="Blue Whale", c="Giraffe", d="Hippopotamus", ans="Blue Whale"),
            Questions(ques="Which gas do plants absorb from the atmosphere?", a="Oxygen", b="Nitrogen", c="Carbon Dioxide", d="Hydrogen", ans="Carbon Dioxide"),
            Questions(ques="What is the main ingredient in bread?", a="Rice", b="Wheat", c="Corn", d="Barley", ans="Wheat"),
            Questions(ques="Who is known as the Father of Computers?", a="Charles Babbage", b="Alan Turing", c="Bill Gates", d="Steve Jobs", ans="Charles Babbage"),
            Questions(ques="Which organ pumps blood through the body?", a="Liver", b="Heart", c="Lungs", d="Kidneys", ans="Heart"),
            Questions(ques="What is the square root of 64?", a="6", b="7", c="8", d="9", ans="8"),
        ]
        db.session.bulk_save_objects(questions)
        db.session.commit()


@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password. Please register if you do not have an account.')
            return render_template('login.html', form=form, title='Login')
        session['user_id'] = user.id
        session['marks'] = 0
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    if g.user:
        return redirect(url_for('home'))
    return render_template('login.html', form=form, title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        session['marks'] = 0
        return redirect(url_for('home'))
    if g.user:
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/question/<int:id>', methods=['GET', 'POST'])
def question(id):
    form = QuestionForm()
    q = Questions.query.filter_by(q_id=id).first()
    if not q:
        return redirect(url_for('score'))
    if not g.user:
        return redirect(url_for('login'))
    total_questions = Questions.query.count()
    is_last = (id == total_questions)
    form.options.choices = [
        ("a", q.a),
        ("b", q.b),
        ("c", q.c),
        ("d", q.d)
    ]
    if form.validate_on_submit():
        option = form.options.data
        if getattr(q, option) == q.ans:
            session['marks'] += 5
        if is_last:
            return redirect(url_for('score'))
        else:
            return redirect(url_for('question', id=(id+1)))
    return render_template('question.html', form=form, q=q, title='Question {}'.format(id), is_last=is_last)


@app.route('/score')
def score():
    if not g.user:
        return redirect(url_for('login'))
    g.user.marks = session['marks']
    db.session.commit()
    return render_template('score.html', title='Final Score')

@app.route('/logout')
def logout():
    if not g.user:
        return redirect(url_for('login'))
    session.pop('user_id', None)
    session.pop('marks', None)
    return redirect(url_for('home'))

@app.route('/retake')
def retake():
    session['marks'] = 0
    return redirect(url_for('question', id=1))