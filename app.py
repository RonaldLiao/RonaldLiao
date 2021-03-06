from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

logger.debug('Loging %s level', 'DEBUG')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b8561a60879da2f6552981f5fdff5b8c'

posts = [ 
    {
        'author': 'Corey Shafer',
        'title': 'Blog post 1',
        'content': 'first post content',
        'data_posted': 'April 20, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': 'second post content',
        'data_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Log in successful for {form.username.data}!', 'success')
        return redirect(url_for('about'))
    else:
        if form.errors:
            logger.debug(form.errors)
            flash(f'{form.errors}!', 'danger')   
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
    
    
    