echo "Build project..."
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

echo "Make migration..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "Collect static..."
python3.9 manage.py collectstatic --noinput

echo "Create superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root2', 'root2@root.com', 'root2')" | python3.9 manage.py shell
