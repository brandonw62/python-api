# python-api

## Setup And Installation

```bash
git clone <repo-url>
```

### Update Packages

```bash
pip install pip -U
pip install setuptools -U
```

### Setup Python Virtual Env

```bash
python3 -m venv venv
source venv/bin/activate

python3 -m pip install fastapi[all]
python3 -m pip install pylint
python3 -m pip install -U autopep8

pip freeze > requirements.txt
```

## Running The App

```bash
uvicorn main:app --reload
```

## Viewing The App

Go to `http://127.0.0.1:8000`
