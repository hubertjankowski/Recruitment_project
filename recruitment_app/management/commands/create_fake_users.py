import randomuser as randomuser
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from randomuser import RandomUser


# Create fake "x" users
class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            user = RandomUser()
            User.objects.create_user(username=RandomUser.get_username(user), first_name=RandomUser.get_first_name(user),
                                     last_name=RandomUser.get_last_name(user), email=RandomUser.get_email(user),
                                     password=RandomUser.get_password(user),
                                     date_joined=RandomUser.get_registered(user))
