import math
from datetime import datetime

import requests

from models import dbQuery

DATA_IMPORT_BATCH_SIZE = 500  # the maximum number of rows retrieving from Open Payments API


def get_datasets_to_update(program_year_last_update_date_pair):
    """
    Filter the most recent year's General Payment Identifiers from the Open Payment API.

    Returns:
    - Response: Response from the API call.
    """
    url = "https://openpaymentsdata.cms.gov/api/1/metastore/schemas/dataset/items?show-reference-ids=false"

    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Request was successful!")
    else:
        print(f"Request failed with status code {response.status_code}")

    # Extract the most recent year from the 'issued' column
    datasets = response.json()
    datasets_to_update = []
    for item in datasets:
        stored_program_years = program_year_last_update_date_pair.keys()
        dataset_program_year = str(int(item['issued'][:4]) - 1)  # issued date is at the next year of the program year
        dataset_modified_date = datetime.strptime(item['modified'][:10], '%Y-%m-%d').date()

        if (dataset_program_year in stored_program_years
                and dataset_modified_date > program_year_last_update_date_pair.get(dataset_program_year)
                and 'general payments' in item['theme'][0]['data'].lower()):
            datasets_to_update += item.get('distribution')

    return datasets_to_update


def get_update_data_size_from_open_payments_api(distributionId):
    url = "https://openpaymentsdata.cms.gov/api/1/datastore/sql"
    query = "[SELECT COUNT(*) FROM {}]".format(distributionId)  # TODO: filter unchanged results
    print("query: ", query)
    params = {
        'query': query
    }
    try:
        response = requests.get(url, params=params)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request was successful!")
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return int(response.json()[0].get('expression'))


def get_data_from_open_payments_api(offset, limit, distributionId):
    url = "https://openpaymentsdata.cms.gov/api/1/datastore/sql"
    query = "[SELECT * FROM {}][LIMIT {} OFFSET {}]".format(distributionId, limit,
                                                            offset)  # TODO: filter unchanged results
    print("query: ", query)
    params = {
        'query': query
    }
    try:
        response = requests.get(url, params=params)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request was successful!")
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return response.json()


def update_db(dataset_to_update):
    offset = 0
    distribution_id = dataset_to_update['identifier']
    update_data_size = get_update_data_size_from_open_payments_api(distribution_id)
    remaining_batch_import_iterations = math.ceil(update_data_size / DATA_IMPORT_BATCH_SIZE)

    for i in range(remaining_batch_import_iterations):
        rows = get_data_from_open_payments_api(offset=offset, limit=DATA_IMPORT_BATCH_SIZE,
                                               distributionId=distribution_id)
        dbQuery.update_payments_in_bulk(rows)
        offset += DATA_IMPORT_BATCH_SIZE
        print("================== Batch update completes with ending offset ", offset)

    print("================== Data update completes for the distribution {}.".format(distribution_id))


def check_for_updated_data():
    print("Checking updates for General Payment data ...")
    # TODO: remove it after testing
    # program_year_last_update_date_pair = {}
    # program_year_last_update_date_pair['2022'] = '06-30-2022'
    # program_year_last_update_date_pair['2022'] = datetime.strptime(program_year_last_update_date_pair['2022'],
    #                                                                '%m-%d-%Y').date()

    program_year_last_update_date_pair = dbQuery.get_last_update_date_for_program_year()
    datasets_to_update = get_datasets_to_update(program_year_last_update_date_pair)
    for dataset in datasets_to_update:
        update_db(dataset)

    print("================== Data update completes. Updated {} datasets.".format(len(datasets_to_update)))
