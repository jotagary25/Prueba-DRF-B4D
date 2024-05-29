import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

def create_superuser():
    from django.contrib.auth.models import User
    
    # Obtener los valores de las variables de entorno
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin123123')

    # Check if the superuser already exists
    if User.objects.filter(username=username, is_superuser=True).exists():
        # Create a superuser with the given username, email, and password
        print("Superuser already exists.")
    else:
        User.objects.create_superuser(username, email, password)
        print("Superuser created successfully.")

# Llamar a la función para crear el superusuario
create_superuser()
