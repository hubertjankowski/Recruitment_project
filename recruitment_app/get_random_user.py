import random

from django.contrib.auth.models import User


# Get random user from existing user
def random_user():
    items = User.objects.all()
    random_item = random.choice(items)

    return random_item
