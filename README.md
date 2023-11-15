# OpenPayment
A web application to retrieve and query Open Payment Dataset.

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
