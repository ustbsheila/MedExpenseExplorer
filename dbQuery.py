# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 00:26:27 2023

@author: Sheila
"""

from app import db, connection
from models import GeneralPayment
from sqlalchemy import exc

def add_payment(row):
#    new_payment = GeneralPayment(**row)
    db.session.execute(GeneralPayment.__table__.insert().prefix_with('IGNORE'),row)
    
def add_payments_in_bulk(rows):
    for r in rows:
        add_payment(r)
    db.session.commit()

                
def get_general_payment_offset():
    return db.session.query(GeneralPayment).count()
    
def show_tables():
    res = connection.execute('SHOW TABLES')
    return res

def rollback():
    db.session.rollback()