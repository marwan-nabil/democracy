# how to install
---

1. git clone this repo.

2. inside it, make a new virtual environment (to isolate the project environment).   
`python -m venv .venv`

3. activate the virtual environment.   
`.venv\Scripts\activate.bat` on windows.   
`.venv/bin/activate` on linux.

3. install dependencies.   
`pip install -r requirements.txt`   

4. cd into the server directory.   
`cd frontend_server`

5. commit all database operations.   
`python manage.py migrate`

6. run the server.   
`python manage.py runserver`   


# basic architecture
---

![website architecture](documentation\project_architecture.jpg)