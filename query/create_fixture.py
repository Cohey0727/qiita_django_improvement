import random
from .models import *

GROUP_COUNT = 10000
USER_COUNT_BY_GROUP = 100
INVOICE_COUNT_BY_USER = 10


def run():
    # create groups
    groups = [Group(name=f'group_{index}') for index in range(GROUP_COUNT)]
    Group.objects.bulk_create(groups, batch_size=10000)

    # create users
    all_groups = Group.objects.all()
    users = [
        User(name=f'group_{group.id}_user_{index}', group=group)
        for index in range(USER_COUNT_BY_GROUP) for group in all_groups
    ]
    User.objects.bulk_create(users, batch_size=10000)

    # create invoices
    all_users = User.objects.all()
    invoices = [
        Invoice(price=random.randint(1000, 100000), user=user)
        for index in range(INVOICE_COUNT_BY_USER) for user in all_users
    ]
    Invoice.objects.bulk_create(invoices, batch_size=10000)
