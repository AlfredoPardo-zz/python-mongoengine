# Python Mongoengine PoC

This assumes that you have a MongoDB Database with the configuration listed as in config.yaml, and that you're using Linux and Python 3.

1. Create a virtual environment

> $ python3 -m venv venv

2. Activate the virtual environment

> $ source venv/bin/activate

3. Install the requirements

> $ pip install -r requirements.txt

4. Add records to the database

> $ python main.py add-records

5. Show the records in the database

> $ python main.py show-records

6. Delete the records from the database

> $ python main.py delete-records




