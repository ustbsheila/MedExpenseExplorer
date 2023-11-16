# OpenPayment
A web application to retrieve and query Open Payment Dataset.

### Run the web application
You can either run the application in your command line or run it in the docker container.

* Run the Flask application in command line (for local development).
  * Enter the follow command line in the OpenPayment root directory.
    ``` .bash
    python run.py
    ```
  * Visit http://127.0.0.1:5000/ in your web browser, and you should see the blank home page with a clickable button. Clicking the button will import the most recent year's data.

* Run the Flask application in docker container
   ``` .bash
    docker-compose up -d
   ```
  

### Access MySQL docker container
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
USE your_database_name;

-- Show tables in the selected database
SHOW TABLES;

-- Run a SQL query
SELECT * FROM your_table_name;

```