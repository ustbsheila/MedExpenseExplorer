# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 00:03:54 2023

@author: Sheila
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models import db

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
    res = "This is the import page. "
    
    datasets_to_import = dataIngestion.get_most_recent_year_identifiers()
    dataIngestion.import_most_recent_year_data_to_db(datasets_to_import)
    
    exe = connection.execute('select * from GeneralPayment;')
    res += str(exe.fetchall())

    return res



if __name__ == '__main__':
    app.run(debug=True)