# QuickBite

A web application for ordering food from independent restaurants and picking it up. Built with Python and Flask as part of the COMP 354 Assignment 2 (Agile and Scrum).

## Requirements

- Python 3.10 or newer
- Git

## Setup

1. Clone the repository and enter the folder:
```
   git clone https://github.com/eliixar/comp-354-a2.git
   cd comp-354-a2
```

2. Create and activate a virtual environment:

   Windows (PowerShell):
```
   python -m venv venv
   venv\Scripts\activate
```
   Mac/Linux:
```
   python3 -m venv venv
   source venv/bin/activate
```
   If PowerShell blocks the activation script, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and try again.

3. Install the dependencies:
```
   python -m pip install -r requirements.txt
```

4. Set up the database (schema and sample data):
```
   python init_db.py

```

## Run the app

```
python app.py
```
Then open http://127.0.0.1:5000 in your browser. Press Ctrl+C in the terminal to stop it.

## Run the tests

```
pytest
```

## Project structure

- `app.py`: the Flask application
- `templates/`: HTML templates
- `tests/`: automated tests
- `docs/`: Definition of Done and team documents
- `requirements.txt`: Python dependencies
