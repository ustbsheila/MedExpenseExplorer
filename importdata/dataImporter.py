import math

import requests

from models import dbQuery

DATA_IMPORT_BATCH_SIZE = 500  # the maximum number of rows retrieving from Open Payments API


def download_file(url, local_filename):
    response = requests.get(url, stream=True)
    with open(local_filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)


def download_most_recent_year_data_as_csv(datasets_to_import):
    # download files from distributions
    for index, item in enumerate(datasets_to_import):
        uri = item['data']['downloadURL']
        local_filename = str(index) + '_' + item['identifier'] + '.' + item['data']['format']
        download_file(uri, local_filename)


def get_most_recent_year_identifiers():
    """
    Filter the most recent year's General Payment Identifiers from the Open Payment API.

    Returns:
    - Response: Response from the API call.
    """
    url = "https://openpaymentsdata.cms.gov/api/1/metastore/schemas/dataset/items?show-reference-ids=false"

    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request was successful!")
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    # Extract the most recent year from the 'issued' column
    datasets = response.json()
    most_recent_year = max(datasets, key=lambda x: int(x['issued'][:4]))['issued'][:4]

    # Filter the data with the following two conditions: 
    # 1. get the most recent year's data
    # 2. get the General Payments category
    datasets_to_import = []
    for item in datasets:
        if item['issued'][:4] == most_recent_year and 'general payments' in item['theme'][0]['data'].lower():
            datasets_to_import += item.get('distribution')

    return datasets_to_import


def get_data_from_open_payments_api(offset, limit, distributionId):
    """
    Given the datasets needed to import, call Open Payment API to retrieve data in batches and bulk insert to MySQL DB.

    Parameters:
    - offset (int): The number of rows to skip before starting to return results by calling API.
    - limit (int): The maximum number of rows to be returned by the API.
    - distributionId (string): An identity for a container for the data object.

    Returns:
    - Response: Response from the API call.
    """
    # Continue to import data from previous offset
    url = "https://openpaymentsdata.cms.gov/api/1/datastore/query/" + distributionId
    params = {
        'limit': limit,
        'offset': offset,
        'format': 'json'
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

    return response


def import_most_recent_year_data_to_db(dataset_to_import):
    """
    Given the datasets needed to import, call Open Payment API to retrieve data in batches and bulk insert to MySQL DB.

    Parameters:
    - datasets_to_import (list<dict>): The need to import dataset information used for calling API.

    Returns:
    - string: The data import stats to display in the frontend.
    """
    distributionId = dataset_to_import['identifier']

    offset = dbQuery.get_general_payment_offset()
    response = get_data_from_open_payments_api(offset=offset, limit=1,
                                               distributionId=distributionId)  # initial call to get table size
    table_size = response.json().get('count')
    remaining_batch_import_iterations = math.ceil(table_size / DATA_IMPORT_BATCH_SIZE)
    import_status = ("INFO: original table size is {}. Importing dataset from distrution Id {}. "
                     "The process starts from offset {} with {} iterations. ").format(
        table_size, distributionId, offset, remaining_batch_import_iterations)

    for i in range(remaining_batch_import_iterations):
        response = get_data_from_open_payments_api(offset=offset, limit=DATA_IMPORT_BATCH_SIZE,
                                                   distributionId=distributionId)
        rows = response.json().get('results')
        dbQuery.add_payments_in_bulk(rows)
        offset += DATA_IMPORT_BATCH_SIZE
        print("================== Batch import completes with ending offset ", offset)

    offset = dbQuery.get_general_payment_offset()
    return import_status + "Data import completes. Current database has been updated with {} rows.".format(offset)


def start_data_import_process():
    """
    Start the data import process to retrieve the more recent year's General Payment data from Open Payment API
    (openpaymentsdata.cms.gov) and store the data in the connected MySQL DB.

    Returns:
    - string: The data import stats to display in the frontend.
    """
    datasets_to_import = get_most_recent_year_identifiers()
    process_status = "Data import Process: "
    for dataset in datasets_to_import:
        process_status += import_most_recent_year_data_to_db(dataset)

    return process_status
