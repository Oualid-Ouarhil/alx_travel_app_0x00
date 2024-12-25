from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **kwargs):
        listings = [
            Listing(title='Sample Listing 1', description='Description 1', price=100, location='Location 1', available=True),
            Listing(title='Sample Listing 2', description='Description 2', price=150, location='Location 2', available=True),
        ]

        Listing.objects.bulk_create(listings)
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
