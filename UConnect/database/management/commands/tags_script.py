import csv
from database.models import Tag
from django.core.management.base import BaseCommand

# to use: in the F24-Sapphire/UConnect folder, run 'python manage.py tags_script'
class Command(BaseCommand):
    help = "Adds tags to the database."

    def handle(self, *args, **options):
        with open("database/tags.csv") as file:
            reader = csv.reader(file)
            for entry in reader:
                Tag.objects.get_or_create(
                    name = entry[0]
                )
