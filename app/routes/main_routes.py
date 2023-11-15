from flask import render_template, Blueprint
from . import main_bp

@main_bp.route('/')
def home():
    return render_template('index.html')