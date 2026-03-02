import csv
from django.core.management.base import BaseCommand
from myapp.models import Seed

class Command(BaseCommand):
    help = 'Imports seed data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the csv file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    obj, created = Seed.objects.get_or_create(
                        name=row['name'],
                        defaults={
                            'botanical': row['botanical'],
                            'seed_type': row['seed_type'],
                            'continent': row['continent']
                        }
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Imported: {row['name']}"))
                    else:
                        self.stdout.write(self.style.WARNING(f"Skipped: {row['name']}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))