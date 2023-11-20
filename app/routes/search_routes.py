import csv
from io import StringIO

from flask import jsonify
from flask import render_template, Response

from app.forms import SearchForm
from models.generalpayment import GeneralPayment
from . import search_bp


@search_bp.route('/export_csv?<column>&<search_term>')
def export_csv(column, search_term):
    print("CVS export starts.")
    # Retrieve search results from db
    results = GeneralPayment.query.filter(getattr(GeneralPayment, column).ilike(f'%{search_term}%')).all()

    # Convert results to CSV format
    csv_data = StringIO()
    csv_writer = csv.writer(csv_data)

    # Write header
    csv_writer.writerow([column.name for column in GeneralPayment.__table__.columns])

    # Write data rows
    for row in results:
        csv_writer.writerow([getattr(row, column.name) for column in GeneralPayment.__table__.columns])

    # Set up the CSV response
    response = Response(csv_data.getvalue(), content_type='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=search_results.csv'

    print("CVS export completes.")
    return response


@search_bp.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    columns = [column.name for column in GeneralPayment.__table__.columns]

    if form.validate_on_submit():
        column = form.column.data  # entered column
        search_term = form.search_term.data  # entered content
        results = GeneralPayment.query.filter(getattr(GeneralPayment, column).ilike(f'%{search_term}%')).limit(
            100).all()
        return render_template('search_results.html', results=results, column=column, search_term=search_term)

    return render_template('search.html', columns=columns, form=form)


@search_bp.route('/get_search_data_for_typeahead', methods=['GET', 'POST'])
def get_search_data():
    columns = [column.name for column in GeneralPayment.__table__.columns]

    return jsonify(columns)
