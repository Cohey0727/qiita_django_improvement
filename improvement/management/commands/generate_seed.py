import random

from django.core.management.base import BaseCommand

from query.models import Group, User, Invoice
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Generate Seed Data'

    def handle(self, *args, **options):
        groups = []
        print('Groupを作成します。')
        for i in range(100000):
            print("\r{0:s}".format(f"{i + 1}件取込みました。"), end="")
            groups.append(Group(name=fake.name()))

        Group.objects.bulk_create(groups)
        groups = Group.objects.all()

        users = []
        print('\nUserを作成します。')
        for i, group in enumerate(groups):
            for j in range(10):
                print("\r{0:s}".format(f"{((i + 1) * 10 + (j + 1))}件取込みました。"), end="")
                users.append(User(group=group, name=fake.name()))

        User.objects.bulk_create(users)
        users = User.objects.all()

        invoices = []
        print('\nInvoiceを作成します。')
        for i, user in enumerate(users):
            for j in range(5):
                print("\r{0:s}".format(f"{((i + 1) * 10 + (j + 1))}件取込みました。"), end="")
                invoices.append(Invoice(user=user, price=random.randrange(10000, 999999)))

        Invoice.objects.bulk_create(invoices)
