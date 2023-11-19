from app import db
from models.generalpayment import GeneralPayment
from sqlalchemy import select, distinct
from sqlalchemy.sql.expression import func
from datetime import datetime

def add_payment(row):
    """
    Insert a row to General Payment table in DB. Skip if the primary key record ID exists.
    """
    db.session.execute(GeneralPayment.__table__.insert().prefix_with('IGNORE'), row)


def add_payments_and_handle_error(rows):
    """
    Individual insert rows to General Payment table in DB. Log error message if exception throws.
    """
    for r in rows:
        try:
            add_payment(r)
            db.session.commit()
        except Exception as err:
            print("Insert error. Details: {}. Skip inserting this row. {}".format(err, r))


def add_payments_in_bulk(rows):
    """
    Bulk insert rows to General Payment table in DB. Skip if the primary key record ID exists.
    """
    try:
        for r in rows:
            add_payment(r)
        db.session.commit()
    except Exception:
        rollback()
        add_payments_and_handle_error(rows)


def get_general_payment_offset():
    """
    Get current offset for the General Payment table in the database.
    """
    return db.session.query(GeneralPayment).count()


def get_last_update_date_for_program_year():
    """
    Get last update date for each program year from the database.
    """
    stmt = select([func.max(GeneralPayment.payment_publication_date), GeneralPayment.program_year]).group_by(GeneralPayment.program_year)
    result = db.session.execute(stmt)
    res = {}

    for item in result.all():
        last_update_date = item[0]
        program_year = item[1]
        if last_update_date and program_year: # parse information only if both program year and last update date exist
            last_update_date = datetime.strptime(last_update_date, '%m/%d/%Y').date() # convert string to date
            res[program_year] = last_update_date

    return res

def update_payment(row):
    """
    Insert a row to General Payment table in DB. Skip if the primary key record ID exists.
    """
    # db.session.query(GeneralPayment).filter(GeneralPayment.record_id == row.get("Record_ID")).update(row)
    general_payment = GeneralPayment.query.get(row.get("Record_ID"))
    if general_payment:
        for key, value in row.items():
            setattr(general_payment, key, value)
        db.session.commit()
        print("GeneralPayment updated successfully.")

def update_payments_in_bulk(rows):
    """
    Bulk insert rows to General Payment table in DB. Skip if the primary key record ID exists.
    """
    for r in rows:
        try:
            update_payment(r)
        except Exception as err:
            rollback()
            print("Insert error. Details: {}. Skip inserting this row. {}".format(err, r))

def update_payments_and_handle_error(rows):
    """
    Individual insert rows to General Payment table in DB. Log error message if exception throws.
    """
    for r in rows:
        try:
            update_payment(r)
            db.session.commit()
        except Exception as err:
            print("Update error. Details: {}. Skip updating this row. {}".format(err, r))

def rollback():
    """
    Rollback last database transaction.
    """
    db.session.rollback()