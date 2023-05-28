# gs-auto-ml

Project developed for the Global Solution of the Automated Machine Learning &amp; Mobile Deploy subject

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-31010/)
[![PEP20](https://img.shields.io/badge/code%20style-pep20-red.svg)](https://www.python.org/dev/peps/pep-0020/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![bandit](https://img.shields.io/badge/code%20style-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Technology and Resources

- [Python 3.10](https://www.python.org/downloads/release/python-31010/) - **pre-requisite**
- [Docker](https://www.docker.com/get-started) - **pre-requisite**
- [Docker Compose](https://docs.docker.com/compose/) - **pre-requisite**
- [Pipenv](https://github.com/pypa/pipenv)
- [Flask](https://flask.palletsprojects.com/en/2.3.x)
- [Waitress](https://docs.pylonsproject.org/projects/waitress/en/latest/index.html)

*Please pay attention on **pre-requisites** resources that you must install/configure.*

### How to Install

```
make local/install
```

### How to Build

```
make docker/build
```

### How to Run

```
make local/run
make docker/run
```

*The project will be running at `http://localhost:5000/`*

The `entrypoint` of this project is the `run.py` file on the root path.

### How to lint

`make docker/lint` or `make local/lint` to lint

`make docker/bandit` or `make local/bandit` to execute the bandit check

`make docker/check-packages` or `make local/check-packages` to check for packages vulnerabilities

**Helpful commands**

*Please, check all available commands in the [Makefile](Makefile) for more information*.
