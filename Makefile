run:
	python3 manage.py runserver 0.0.0.0:8787

install:
	pip install -r requirements.txt

replit:
	make install
	make run