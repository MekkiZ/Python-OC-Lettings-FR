web: gunicorn --bind 0.0.0.0:$PORT oc_lettings_site:app
python3 manage.py collectstatic --noinput
manage.py migrate