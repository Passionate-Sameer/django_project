Download and unzip the repo
    django_project

CD to the project directory
    cd django_project

Activate the virtual environment. It is recommended to run in virtual environment.
    source py310_venv/bin/activate

Install all project dependencies
    pip install requirements.py

Apply the migrations
    python manage.py migrate

Create an .env file at the same level as django_project/settings.py file
    touch .env

Write API key that is to connect to news api. Save and close the file.
    API_KEY='write api key'

Run the dev-server
    python manage.py runserver

Open Browser and access the below links
    For API view (json)
        http://127.0.0.1:8000/api
    For list view (html)
        http://127.0.0.1:8000/

Note:   During first run, access the api link first. 
        The api endpoint fetches the latest news data from news api and 
        populates the database. The database will be empty during the 
        first run, so populating of the database is required to display
        the news items in the html view.