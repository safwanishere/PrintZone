from flask import Blueprint, render_template, request, redirect, url_for, flash, session

admin = Blueprint('admin', __name__)

@admin.route('/', methods=["GET", "POST"])
def admin_panel():
    return render_template('index.html')