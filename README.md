# 🌳 ForestWork
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/ElveeBolt/forestwork)
[![Supported python versions](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/downloads/)
[![Code style](https://img.shields.io/badge/code%20style-PEP8-blue)](https://peps.python.org/pep-0008/)

**Forestwork** - job search service for developers and employers.


## Installing ForestWork

```bash
# Clone this repo and create virtual environment
git clone https://github.com/ElveeBolt/Forestwork.git
cd Forestwork

# For Linux/Ubuntu
python3 -m venv venv
source venv\bin\activate
pip install -r requirements.txt

# For Windows
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Installing with Docker Compose
```bash
# Clone this repo and and build docker containers
git clone https://github.com/ElveeBolt/Forestwork.git
cd Forestwork

docker compose up --build
```

## Run ForestWork
```bash
python manage.py runserver
```

After starting, you can go to http://127.0.0.1:8000/ and use ForestWork app

## Author
Developed and maintained by [ElveeBolt](https://github.com/ElveeBolt).

Thanks to everybody that has contributed pull requests, ideas, issues, comments and kind words.