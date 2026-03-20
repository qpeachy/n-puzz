.PHONY: help install test lint format clean run

help:
	@echo "Available commands:"
	@echo "  make install - Install dependencies"
	@echo "  make test - Run tests"
	@echo "  make lint - Run linting"
	@echo "  make format - Format code"
	@echo "  make clean - Remove build artifacts"
	@echo "  make Run - Run the application"

install:
	pip install -r requirements.txt

test:
	pytest

lint:
	pylint *.py
	flake8 *.py

format:
	black *.py
	isort *.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache .coverage

run:
	python3 main.py