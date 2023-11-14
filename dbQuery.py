# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 00:26:27 2023

@author: Sheila
"""

from app import db, connection
from models import GeneralPayment
from sqlalchemy import exc

def add_payment(row):
    new_payment = GeneralPayment(**row)
    db.session.add(new_payment)
    db.session.commit()
    
def add_payments(rows):
    for r in rows:
        try:
            add_payment(r)
        except exc.IntegrityError as err:
            rollback()
            if "Duplicate entry" in str(err):
                print ("Duplicate key, skipping this row.")
                
def add_payments_in_bulk(rows):
    try:
        db.session.bulk_insert_mappings(GeneralPayment, rows)
        db.session.commit()
    except exc.IntegrityError as err:
        rollback()
        if "Duplicate entry" in str(err):
            print ("Duplicate key, skipping this row.")
    
def get_general_payment_offset():
    return db.session.query(GeneralPayment).count()
    
def show_tables():
    res = connection.execute('SHOW TABLES')
    return res

def rollback():
    db.session.rollback()