# Drones (Musala Soft task)

### Download and active enviroment

Config virtualenv:

```bash
git clone https://github.com/eadomenech/drones.git
```

```bash
cd drone
```

```bash
python3.8 -m venv env
```

```bash
source env/bin/activate
```

```bash
python -m pip install -U pip
```

```bash
pip install -r requiremets.txt
```

```bash
cd src
```

```bash
uvicorn app.main:app
```

Run tests:

```bash
pytest
```

Code quality:

```bash
$ flake8 app
```

### Docker

Create requirements image:

```bash
docker build -f src/Dockerfile-requirements --tag drones_requirements .
```

Create container:

```bash
docker-compose up --build
```

Run tests:

```bash
docker-compose run --rm api pytest
```

Code quality:

```bash
docker-compose run --rm api flake8 app
```

### API docs:

* http://localhost:8001/docs
* http://localhost:8001/redoc