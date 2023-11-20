# MedExpense Explorer

MedExpense Explorer is a Python Flask Web Application  that provides access to information from the [Open Payments API](https://openpaymentsdata.cms.gov/about/api). It allows users to import the most recent year's data, checks regularly for updates, provides a search tool with a typeahead, and includes an "Export to Excel" feature for search results.

## Features

1. **Import Most Recent Year's Data:**
   - The application allows users to import the most recent year's data from the [Open Payments API](https://openpaymentsdata.cms.gov/about/api).

2. **Regular Updates:**
   - The application automatically checks for and fetches the most recent updates from the Open Payments API on a regular basis (every 24 hours).

3. **Search Tool with Typeahead:**
   - A powerful search tool with typeahead functionality enables users to quickly find relevant data. It supports searching one field. We may support searching across multiple fields in future.

4. **Export to Excel:**
   - Once search results are retrieved, users can export the data to an Excel file (XLS). This feature provides a convenient way to analyze and share the obtained information.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ustbsheila/MedExpenseExplorer.git

2. Run the web application
You can either run the application in your command line or run it in the docker container.
   * Run the Flask application in command line (for local development):
     * Install dependencies:
          ``` .bash
            pip install -r requirements.txt
          ```
     * Run MySQL db in the docker container
       ``` .bash
       docker-compose up -d mysql
       ```
     * Enter the follow command line in the OpenPayment root directory.
       ``` .bash
       python run.py
       ```
     * Visit http://127.0.0.1:5000/ in your web browser, and you should see the blank home page with a clickable button. Clicking the button will import the most recent year's data.

   * Run the Flask application in docker container:
      ``` .bash
       docker-compose up -d
      ```
     * Navigate to http://localhost:5000/ in the browser to interact with the web application.

## Usage

### 1. Import Data:

Navigate to http://127.0.0.1:5000/ in the web browser and click `Import Data` button to start import the most recent year's general payment data from Open Payments API. 

> **_NOTE:_** Do not repeatedly click the button quickly. It may take hours to finish data import. The import can be resumed from previous location if the application restarts.

### 2. Search Tool:

Navigate to http://127.0.0.1:5000/search in the web browser. Use the search tool to perform searches with typeahead functionality.

### 3. Export to Excel:
    
After performing a search, click on the "Export to Excel" button to download the search results in an Excel file.

### Access MySQL docker container
You can access MySQL DB to explore or validate backend data.

1. Enter the following command line in the terminal

```commandline
docker exec -it mysql-db mysql -u ustbsheila -p
```

2. Enter MySQL password `12345` when the request is prompted. 

3. Interact with MySQL using MySQL queries. For example:

```commandline
-- Show databases
SHOW DATABASES;

-- Use a specific database
USE openpaymentdb;

-- Show tables in the selected database
SHOW TABLES;

-- Run a SQL query
SELECT COUNT(*) FROM GeneralPayment;

```