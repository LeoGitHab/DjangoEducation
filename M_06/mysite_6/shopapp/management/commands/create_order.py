from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order


class Command(BaseCommand):
    """
    Create orders
    """

    def handle(self, *args, **options):
        self.stdout.write('Create order:')
        user = User.objects.get(username='leodjango')

        order = Order.objects.get_or_create(
            delivery_address='Pushkin street, house 2',
            promocode='SALE123',
            user=user,
        )

        self.stdout.write(self.style.SUCCESS(f'Created order {order}'))
