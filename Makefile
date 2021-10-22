# Globals; we can override this by passing the env var in the
# invocation command.
SHELL := /bin/bash
ENVIRONMENT ?= develop

.PHONY: help

help: ## execute this help command
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %", $$1, $$2}' $(MAKEFILE_LIST)

dev: ## setup the local development environment
	@echo "verifying python local enviornmen"
	if [ ! -d "venv" ]; then python3 -m venv venv && source venv/bin/activate && pip install pip --upgrade && pip install -r requirements.txt; fi
	
	@echo "python environment ready";
	@echo "run source venv/bin/activate in another terminal tab";

	@echo "deleting local postgresql data"
	docker compose down;
	rm -rf ./postgres-data;

	@echo "starting database(s)";
	docker compose up --detach redis postgres;
	@echo "running migrations";


	venv/bin/python django/backend/scripts/is_database_ready.py --database postgres://omni:omni@localhost:5433/omni;
	venv/bin/python django/manage.py makemigrations;
	venv/bin/python django/manage.py migrate;
	venv/bin/python django/manage.py runserver;


migrate:  ## runs migrations.
	venv/bin/python django/manage.py makemigrations;
	venv/bin/python django/manage.py migrate;

test: ## runs test test suite.
	@echo "running python test suit"
	source venv/bin/activate && cd django/ && python3 manage.py test;

coverage: ## generates coverate report.
	@echo "generating coverage report"
	source venv/bin/activate && coverage report;
	source venv/bin/activate && coverage html;

tail-logs: ## tails logs from runningn app.
	heroku logs --tail;

##############################################################
#    ______   _______  __   __  _______  _______  _______    #
#   |      | |       ||  | |  ||       ||       ||       |   #
#   |  _    ||    ___||  |_|  ||   _   ||    _  ||  _____|   #
#   | | |   ||   |___ |       ||  | |  ||   |_| || |_____    #
#   | |_|   ||    ___||       ||  |_|  ||    ___||_____  |   #
#   |       ||   |___  |     | |       ||   |     _____| |   #
#   |______| |_______|  |___|  |_______||___|    |_______|   #
#                                                            #
##############################################################