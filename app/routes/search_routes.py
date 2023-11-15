from flask import render_template, Blueprint, Response, session
from app.forms import SearchForm
from models.generalpayment import GeneralPayment
from . import search_bp
from app import db

import csv
from io import StringIO

@search_bp.route('/export_csv')
def export_csv():
    print("CVS export starts.")
    # Retrieve search results from the session
    results = session.get('search_results')

    # Convert results to CSV format
    csv_data = StringIO()
    csv_writer = csv.writer(csv_data)

    # Write header
    csv_writer.writerow([column.name for column in GeneralPayment.__table__.columns])

    # Write data rows
    for row in results:
        csv_writer.writerow([row.get(column.name) for column in GeneralPayment.__table__.columns])

    # Set up the CSV response
    response = Response(csv_data.getvalue(), content_type='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=search_results.csv'

    print("CVS export completes.")
    return response


@search_bp.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()

    if form.validate_on_submit():
        search_term = form.search_term.data
        results = GeneralPayment.query.filter(GeneralPayment.change_type.ilike(f'%{search_term}%')).limit(5).all()
        session['search_results'] = [GeneralPayment.row2dict(result) for result in results]  # Store results in the session

        return render_template('search_results.html', results=results)

    return render_template('search.html', form=form)