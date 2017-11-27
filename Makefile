init:
	pipenv install --dev

ci:
	pipenv run pytest -vv ./tests -m 'not system' --junitxml=reports/pytest/junit.xml
