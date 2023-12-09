pip install -r requirements.txt

# run tests
pytest --cov=. --cov-fail-under=100 && exit 1 || exit 0