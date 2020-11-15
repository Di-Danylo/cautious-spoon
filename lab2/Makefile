all: install test run deploy

install:
	@echo "Installing pipenv and dependencies."
	pip3 install pipenv
	pipenv --python 3.8
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	@echo "Run app.py "
	pipenv run python3 app.py > results.txt

run:
	@echo "Run tests.py"
	pipenv run pytest tests/tests.py >> results.txt

deploy:
    @echo "git commit/push файла results.txt"
	git add results.txt && git commit -m "додаємо results.txt" && git push
