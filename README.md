# python-cli
A command line app for money spends management

# Installation steps

### 1. Install Python dependencies (for Ubuntu):
`sudo apt install python3 python3-pip python3-venv`<br>

### 2. Clone repo by running:
`git clone https://github.com/triple-ua/python-cli.git`

### 3. Change your working directory to project root folder:
`cd python-cli/`

### 4. Create a virtual environment by running:
`python3 -m venv venv`

### 5. Activate your virtual environment:
`source venv/bin/activate`<br>
<br>***(venv)*** in front of your prompt means everything is OK and you're working in local virtual environment of the project<br>
<br>(when you're done just call `deactivate` to deactivate a virtual environment)

### 6. Install all requirements a project uses:
`pip install -r requirements.txt`

### 7. Configure a database settings in `./database/database.py`<br>
You shouldn't choose a name of existing database. Script in step 8 is creating a new database with specified name

### 8. Initialize database and fill tables with data:
`python app/database/config/db_init.py`

### 9. Run a program:
`python app/main.py`

# About program

Program works with strongly defined tables `users` and `spends`:<br>
<br>*users:*
|id|login|password|status|
|--|-----|--------|------|

<br>*spends:*
|id|category|user_id|spends|date|
|--|--------|-------|------|----|

There are convention of methods calls. Right and only way to call a method with specified parameters is:
<br>`method_name param1:value1 param2:value2` and so on...

Method signatures are shown by calling `h`-method in program
