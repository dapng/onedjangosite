echo "Build project..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Make migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "Collect static..."
python manage.py collectstatic --noinput
