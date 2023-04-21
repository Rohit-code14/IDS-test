import sqlite3
import uuid
from flask import Blueprint, redirect, render_template, url_for, session, request
from .dbUtils import *
auth =  Blueprint("auth", __name__, url_prefix="/")
import jwt

def generate_jwt(email):
    secret = "thisisasecret"
    payload = {"email": email}
    token = jwt.encode(payload, secret, algorithm="HS256")
    return token

@auth.route("/")
@auth.route("/register", methods=['GET','POST'])
def register():
    if(request.method == 'GET'):
        if 'auth' in session:
            if session['auth']:
                # return redirect(url_for('feature.dashboard'))
                return render_template("chart.html")
        return render_template("register.html")
    
    elif(request.method == 'POST'):

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        companyname = request.form['companyname']
        apikey = generate_jwt(email)
        print("token -> ",apikey)
        res = retrieveUsers(email)

        if res!=None and res.__len__() != 0:
            return render_template("login.html",message="Account already Exist!!")

        insertUser(email,password,companyname, name,apikey)

        return redirect(url_for('auth.login'))
    
    else:
        return "404 not found"

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'GET'):
        if 'auth' in session:
            if session['auth']:
                return redirect(url_for('feature.dashboard'))
        return render_template("login.html")
    elif(request.method == 'POST'):
        email=request.form['email']
        password=request.form['password']

        resp = verifyUsers(email,password)

        if resp!=None and resp.__len__()!=0:
            session['auth'] = True
            session['email'] = email
            session['name'] = resp[4]
            session['uid'] = resp[0]
            # return redirect(url_for('feature.dashboard'))
            return render_template("chart.html")
        else:
            return render_template("login.html",message="Invalid Credentials!!")
    else:
        return "404 not found"
    
@auth.route('/logout')
def logout():
    session.pop('email',None)
    session.pop('name',None)
    session['auth'] = False
    session.clear()
    return redirect(url_for('auth.login'))