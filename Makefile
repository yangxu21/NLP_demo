install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		pip install -U textblob
	python -m textblob.download_corpora
	
test:
	python -m pytest -vv --cov=wikiphrases --cov=nlplogic test_*.py

format:
	black *.py nlplogic/*.py

lint: 
	pylint --disable=R,C,E1120 *.py nlplogic/*.py

all: install format lint test