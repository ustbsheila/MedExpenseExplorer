# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 23:51:19 2023

@author: Sheila
"""

CREATE DATABASE OpenPaymentDB;
CREATE USER 'ustbsheila'@'localhost' IDENTIFIED BY '12345';
GRANT ALL PRIVILEGES ON GeneralPayments.* TO 'ustbsheila'@'localhost';
FLUSH PRIVILEGES;
