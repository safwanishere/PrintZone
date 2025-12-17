from flask import Blueprint, render_template, request, redirect, url_for, flash, session

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')



@views.route('/contact')
def contact():
    return render_template('contact.html')