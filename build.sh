set -o errexit

pip install requirements.txt

python manage.py migrate

python manage.py collectstatic