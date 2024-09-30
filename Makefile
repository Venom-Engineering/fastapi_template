PHONY: requirements requirements-dev requirements-test test deploy_local

requirements:
	poetry export --without-hashes --without=dev,test --format=requirements.txt > requirements.txt

requirements-test:
	poetry export --without-hashes --only=test --format=requirements.txt > requirements-test.txt

requirements-dev:
	poetry export --without-hashes --only=dev --format=requirements.txt > requirements-dev.txt

test:
	pytest --cov=schema --cov=routers --cov-report term-missing -vv

pylint:
	pylint --generate-rcfile > .pylintrc

deploy_local:
	bash local_deploy.sh