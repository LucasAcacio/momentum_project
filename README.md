# wedostuff

## Start backend:
source venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt
FLASK_APP=main.py FLASK_ENV=development flask run

## Start frontend:
ng serve --port 4200 --host 0.0.0.0 --proxy-config proxy.conf.json
