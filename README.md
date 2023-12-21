# yadiAi

pip3 install -r requirements.txt

run DEV

flask --app app run



#Prod
gunicorn --config gunicorn_config.py app:app 



https://flask.palletsprojects.com/en/3.0.x/installation/#virtual-environments