import os
from django.conf import settings
from django.core.management.base import BaseCommand
from authapp.models import userAccount

class Command(BaseCommand):

    def handle(self, *args, **options):
        if userAccount.objects.count() == 0:
            email = os.environ.get("ADMIN_EMAIL")
            name = os.environ.get("ADMIN_NAME")
            password = os.environ.get("ADMIN_PASSWORD")
            admin = userAccount.objects.create_superuser(email=email, name = name,password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')