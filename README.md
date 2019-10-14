# shout

A Twitter-like application. It's possible to scale it up using cloud services like those provided by AWS or GCP.

## Setup application

1. ``virtulenv venv``
2. ``source venv/bin/active``
3. ``pip install -r requirements.txt``
4. ``python app.py``

You server should be started by now.

## Run tests

1. ``pip install -r tests/requirementst.txt``
2. ``python -m unittest discover .``

Alternatively you can use `nosetests` in order to execute tests.
Application should be running when executing tests.
In order to discover API url please take a look into `app.py` file or related test files.

## Todos

1. To improve error handlig
2. To make application idiot-proof
3. To improve docstrings
4. To ensure code quality by checking code coverage (by tests) and other checks (probably using CI/CD)
5. To switch database from SQLite to production setup (MySQL or PostgreSQL probably)
6. To build docker image
7. To automate deployment using provisionig tools, probably Ansible or similar
