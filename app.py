# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 00:03:54 2023

@author: Sheila
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models import db


def create_app():
    app = Flask(__name__)

    # Load configuration from a separate Config class
    app.config.from_object(Config)

    # Register blueprints and other configurations here

    return app

app = Flask(__name__)

app.config['SQLALCHEMY_ECHO'] = True
engine = create_engine(
      "mysql+pymysql://ustbsheila:12345@localhost:3306/openpaymentdb")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ustbsheila:12345@localhost:3306/openpaymentdb'
db.init_app(app)
connection = engine.connect()

import dataIngestion


# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/import')
def import_data():
    res = "============Importing Open Payments Datasets.============\n"
    
    datasets_to_import = dataIngestion.get_most_recent_year_identifiers()
    res += dataIngestion.import_most_recent_year_data_to_db(datasets_to_import)

    return res



if __name__ == '__main__':
    app.run(debug=True)