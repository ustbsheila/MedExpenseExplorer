# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:20:13 2023

@author: Sheila
"""

import requests
import dbQuery

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
            print("Response content:")
            print(response.text)
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

def import_most_recent_year_data_as_csv(datasets_to_import):
    # download files from distributions
    for index, item in enumerate(datasets_to_import):
        uri = item['data']['downloadURL']
        local_filename = str(index) + '_' + item['identifier'] + '.' + item['data']['format']
        download_file(uri, local_filename)
        

def import_most_recent_year_data_to_db(datasets_to_import):
    dbQuery.add_payment(record_id='12345', change_type = 'NEW', payment_publication_date = '2022-10-09')
