# Some notes and documentation for any potential future devs

## Jinja2 Notes

The j2 files are jinja2 template files. They get rendered by "render_template()" into actual html-files to be served to users.
You should be able to change the file extension to whatever you please, as long as all references are changed accordingly.
The advantage of j2 over html file extension for jinja2 template files is correct syntax highlighting and correct error handling for python/flask variables inserted into script tags.

## Better Comments

If you are using VSCode I recommend installing the extension "Better Comments" by Aaron Bond. It allows for some highligting for various comments. There might be equivalent extensions for other code editors like Pycharm.

## File Structure

The structure of the app itself is as follows:

    .
    ├── .env	# environment variables imported by flask
    ├── main.py	# main file for the app:  "python main.py"
    ├── base.py # base file for unseparated challenges
    ├── helper.py # helper/repeat code functions
    ├── dbconnection.py # sqlite/database connection
    ├── crypto.py
    ├── pass_crack.py
    ├── sql_injection.py
    ├── traversal.py
    ├── templates	# jinja2 template files (.j2)
    │   ├── base.j2
    │   ├── index.j2
    │   ├── ...
    │   ├── crypto
    │   │   ├── cipher.j2
    │   │   ├── hash.j2
    │   │   ├── hash2.j2
    │   ├── pass_crack
    │   │   ├── uauth.j2
    │   │   ├── success.j2
    │   │   ├── ...
    │   ├── sql_injection
    │   │   ├── uauth1.j2
    │   │   ├── uauth2.j2
    │   │   ├── ...
    │   ├── Traversal
    │   │   ├── dir_fail.j2
    │   │   ├──...
    ├── static
    │   ├── css
    │   │   ├── style.css
    │   │   ├──...
    │   ├── js
    │   │   ├── dropdown.js
    │   │   ├──...
    │   ├── img
    │   │   ├──favicon.ico
    │   │   ├──...
    ├──poetry.lock
    ├──pyproject.toml
    ├──user_db.db

There are also the files "dbcheck.py" and "dbreset.py" which are used to check the database and reset it. They are not used by the app itself, but are used by the admin to check that all rows in the table are correct and if not, to reset the table.

Other files such as ".replit" are from replit and are not relevant for the app itself. The may not be present in the final version of the repo.

Before running the app, you need to install the dependencies listed in pyproject.toml. I recommend using poetry for this. You can install poetry with "pipx install poetry" (if pipx is installed) and then run "poetry install" in the directory to install the dependencies. You should then see a new directory called ".venv" in the directory. This is the virtual environment for the app. You can activate it with "poetry shell" and then run the app with "python run.py".

**NB:** The code uses features from python 3.10, so you need to use python 3.10 or higher to run the app. The pyproject.toml file specifies the python version to be 3.10, so poetry should warn you if you are using an incompatible version.
