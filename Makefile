APP_NAME="gs-auto-ml"
IMAGE_NAME="eduardomatoss/gs-auto-ml"
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
    DOCKER_USER=$(shell id -u $(USER)):$(shell id -g $(USER))
endif
ifeq ($(UNAME_S),Darwin)
    DOCKER_USER=
endif

################################
# COMMANDS TO RUN LOCALLY
################################

local/install:
	pipenv install --dev --skip-lock

local/lint:
	black app/
	flake8 app/

local/check-packages:
	pipenv check --system -e PIPENV_PYUP_API_KEY=""

local/bandit:
	bandit -r . app *.py

local/shell:
	pipenv shell

local/run:
	python run.py

############################################
# COMMANDS TO RUN USING DOCKER (RECOMMENDED)
############################################

docker/build:
	CURRENT_UID=${DOCKER_USER} docker-compose build ${APP_NAME}

docker/up:
	CURRENT_UID=${DOCKER_USER} docker-compose up -d

docker/down:
	CURRENT_UID=${DOCKER_USER} docker-compose down --remove-orphans

docker/lint:
	CURRENT_UID=${DOCKER_USER} docker-compose run ${APP_NAME} black app/
	CURRENT_UID=${DOCKER_USER} docker-compose run ${APP_NAME} flake8 app/

docker/check-packages:
	CURRENT_UID=${DOCKER_USER} docker-compose run -e PIPENV_PYUP_API_KEY="" ${APP_NAME} pipenv check --system

docker/bandit:
	CURRENT_UID=${DOCKER_USER} docker-compose run ${APP_NAME} bandit -r . app *.py

docker/verify:
	make docker/lint
	make docker/bandit

docker/run:
	CURRENT_UID=${DOCKER_USER} docker-compose run --service-port ${APP_NAME} python run.py

##################
# HELPFUL COMMANDS
##################

image/build:
	docker build . --target production -t ${IMAGE_NAME}:${VERSION}

image/push:
	docker push ${IMAGE_NAME}:${VERSION}
