# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 23:59:21 2023

@author: Sheila
"""
import app
from app import db

with app.app_context():
    db.create_all()
