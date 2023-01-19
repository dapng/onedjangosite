echo "Build project..."
python3.10 -m pip install --upgrade pip
python3.10 -m pip install -r requirements.txt

echo "Make migration..."
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput

echo "Collect static..."
python3.10 manage.py collectstatic --noinput
