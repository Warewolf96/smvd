from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)
 
app = Flask(__name__)
app.secret_key = os.urandom(12)

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('table.html')
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
 
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/yrc')
def yrc():
    form = ReusableForm(request.form)
    return render_template('yrc.html', form=form)

@app.route('/fif')
def fif():
    form = ReusableForm(request.form)
    return render_template('fif.html', form=form)

@app.route('/sa')
def sa():
    form = ReusableForm(request.form)
    return render_template('sa.html', form=form)

@app.route('/ws')
def ws():
    form = ReusableForm(request.form)
    return render_template('ws.html', form=form)

@app.route('/os')
def os():
    form = ReusableForm(request.form)
    return render_template('os.html', form=form)

@app.route('/ic')
def ic():
    form = ReusableForm(request.form)
    return render_template('ic.html', form=form)

@app.route('/icer')
def icer():
    form = ReusableForm(request.form)
    return render_template('icer.html', form=form)

@app.route('/sr')
def sr():
    form = ReusableForm(request.form)
    return render_template('sr.html', form=form)

@app.route('/sg')
def sg():
    form = ReusableForm(request.form)
    return render_template('sg.html', form=form)

@app.route('/ban')
def ban():
    form = ReusableForm(request.form)
    return render_template('ban.html', form=form)

@app.route('/aus')
def aus():
    form = ReusableForm(request.form)
    return render_template('aus.html', form=form)

@app.route('/ar')
def ar():
    form = ReusableForm(request.form)
    return render_template('ar.html', form=form)

@app.route('/bha')
def bha():
    form = ReusableForm(request.form)
    return render_template('bha.html', form=form)

@app.route('/gb')
def gb():
    form = ReusableForm(request.form)
    return render_template('gb.html', form=form)

@app.route('/jtb')
def jtb():
    form = ReusableForm(request.form)
    return render_template('jtb.html', form=form)

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=4000)
