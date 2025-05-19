import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hoghoogh.settings')
django.setup()

from django.contrib.auth.models import User

# Avoid duplicate users if you rerun the script
if not User.objects.filter(username='admin2').exists():
    User.objects.create_user(username='admin2', password='adminpass2', is_staff=True)
    print("Admin user created.")

if not User.objects.filter(username='user2').exists():
    User.objects.create_user(username='user2', password='userpass2', is_staff=False)
    print("Regular user created.")