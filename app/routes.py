from flask import render_template, flash, url_for, redirect

from app import app
from app.forms import TripSignupForm
from app.models import Trip


@app.route('/')
@app.route('/index')
def index():
    trips = [Trip(
        title='Rock Climbing at J-Tree!!',
        activity='Rock Climbing',
        location='Joshua Tree National Park',
        cost=25)]
    return render_template('index.html', trips=trips)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = TripSignupForm()
    if form.validate_on_submit():
        flash('Signup successful!')
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)
