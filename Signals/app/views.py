from django.contrib.auth.models import User
from django.utils.timezone import now
from django.http import HttpResponse
from django.db.utils import IntegrityError


def create_user(request):
    print(f"User save triggered at: {now()}")
    
    # Start with the base username
    base_username = "test_user"
    username = base_username
    counter = 1

    # Find a unique username
    while User.objects.filter(username=username).exists():
        username = f"{base_username}_{counter}"
        counter += 1

    try:
        # Create the new user with a unique username
        user = User.objects.create(username=username)
        print(f"User save finished at: {now()}")
        return HttpResponse(f"User '{username}' created successfully.")
    
    except IntegrityError:
        return HttpResponse(f"Error: Could not create user '{username}'.")

