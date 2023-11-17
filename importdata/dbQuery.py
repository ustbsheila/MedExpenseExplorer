from app import db
from models.generalpayment import GeneralPayment


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
            print("Insert error. Details: ", err)


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


def rollback():
    """
    Rollback last database transaction.
    """
    db.session.rollback()
