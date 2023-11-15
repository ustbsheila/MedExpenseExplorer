# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:20:13 2023

@author: Sheila
"""

import math
import requests
from . import dbQuery

DATA_IMPORT_BATCH_SIZE = 500 # the maximum number of rows retrieving from Open Payments API

def download_file(url, local_filename):
    response = requests.get(url, stream=True)
    with open(local_filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)

def get_most_recent_year_identifiers():           
    # Replace this with the URL you want to send a GET request to
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
    
    # Filter the data to include identifiers with the most recent year
    datasets_to_import = []
    for item in datasets:
        if item['issued'][:4] == most_recent_year:
            datasets_to_import += item.get('distribution')
            
    return datasets_to_import

def download_most_recent_year_data_as_csv(datasets_to_import):
    # download files from distributions
    for index, item in enumerate(datasets_to_import):
        uri = item['data']['downloadURL']
        local_filename = str(index) + '_' + item['identifier'] + '.' + item['data']['format']
        download_file(uri, local_filename)
        
def get_data_from_open_payments_api(offset, limit, distributionId):
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

def import_most_recent_year_data_to_db(datasets_to_import):
    distributionId = datasets_to_import[-1]['identifier']
    
    offset = dbQuery.get_general_payment_offset()    
    response = get_data_from_open_payments_api(offset=offset, limit=1, distributionId=distributionId) # initial call to get table size
    table_size = response.json().get('count')
    remaining_batch_import_iterations = math.ceil(table_size / DATA_IMPORT_BATCH_SIZE)
    import_status = "INFO: original table size is {}. Importing dataset from distrution Id {}. The process starts from offset {} with {} iterations. ".format(table_size, distributionId, offset, remaining_batch_import_iterations)

    for i in range(remaining_batch_import_iterations):
        response = get_data_from_open_payments_api(offset=offset, limit=DATA_IMPORT_BATCH_SIZE, distributionId=distributionId)
        rows = response.json().get('results')
        dbQuery.add_payments_in_bulk(rows)
        offset += DATA_IMPORT_BATCH_SIZE
        print ("================== Batch import completes with ending offset ", offset)

    offset = dbQuery.get_general_payment_offset()
    return import_status + "Data import completes. Current database has been updated with {} rows.".format(offset)

def start_data_import_process():
    datasets_to_import = get_most_recent_year_identifiers()
    return import_most_recent_year_data_to_db(datasets_to_import)