up:
	docker-compose pull
	docker-compose up --build -d

down:
	docker-compose down

test-env-up:
	docker-compose -f docker-compose-test.yml pull
	docker-compose -f docker-compose-test.yml up --build -d
	DB_DSN=postgresql://test_exness_test:password@localhost:7432/test_exness_test alembic upgrade head

test-env-down:
	docker-compose -f docker-compose-test.yml down

lint:
	pip install -r requirements/dev-requirements.txt
	flake8 src
	pylint src
	mypy src
	black --check --config black.toml src tests

format:
	pip install -r requirements/dev-requirements.txt
	black --verbose --config black.toml src tests alembic

sort:
	pip install -r requirements/dev-requirements.txt
	black --verbose --config black.toml src
	isort src/**/*.py

test:
	pip install -r requirements/test-requirements.txt
	docker-compose -f docker-compose-test.yml pull
	docker-compose -f docker-compose-test.yml up --build -d
	DB_DSN=postgresql://test_exness_test:password@localhost:7432/test_exness_test alembic upgrade head
	pytest -vv --cov src

migrate:
	alembic upgrade head
