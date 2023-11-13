# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 00:26:27 2023

@author: Sheila
"""

import app
from app import db, connection
from models import GeneralPayment

#class GeneralPayment(db.Model):
#    __tablename__ = 'GeneralPayment'
#    RecordId = db.Column(db.String(80), primary_key=True)
#    ChangeType = db.Column(db.String(80))
#    PaymentPublicationDate = db.Column(db.String(80))
#
#    def __repr__(self):
#        return f'<GeneralPayment {self.RecordId}>'

def add_payment(row):
    new_payment = GeneralPayment(**row)
    db.session.add(new_payment)
    db.session.commit()
    
def get_general_payment_offset():
    return db.session.query(GeneralPayment).count()
    
def show_tables():
    res = connection.execute('SHOW TABLES')
    return res

def rollback():
    db.session.rollback()