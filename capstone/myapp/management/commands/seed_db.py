import csv
from django.core.management.base import BaseCommand
from myapp.models import Seed, Use, Donor, DonorProfile

class Command(BaseCommand):
    help = 'Imports relational data while respecting One-to-One constraints'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    # 1. Handle Use
                    use_obj, _ = Use.objects.get_or_create(name=row['use'])

                    # 2. Handle Donors
                    donor_list = []
                    names = row['donors'].split(',')

                    for name in names:
                        name = strip()
                        parts = name.split(' ', 1)
                        f_name = parts[0]
                        l_name = parts[1] if len(parts) > 1 else ""

                        # Check if Donor exists first to avoid profile conflicts
                        donor_obj, d_created = Donor.objects.get_or_create(
                            first_name=f_name,
                            last_name=l_name
                        )

                        # 3. Handle Profile ONLY if the Donor was just created
                        # or if they don't have a profile yet
                        if not hasattr(donor_obj, 'profile') or donor_obj.profile is None:
                            profile_obj = DonorProfile.objects.create(
                                bio=row['bio']
                            )
                            donor_obj.profile = profile_obj
                            donor_obj.save()

                        donor_list.append(donor_obj)

                    # 4. Handle Seed
                    seed, s_created = Seed.objects.get_or_create(
                        name=row['name'],
                        defaults={
                            'botanical': row['botanical'],
                            'seed_type': row['seed_type'],
                            'continent': row['continent'],
                            'use': use_obj
                        }
                    )

                    # 5. Link Many-to-Many
                    for donor in donor_list:
                        seed.donors.add(donor)

                    self.stdout.write(self.style.SUCCESS(f"Processed:{seed.name}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))