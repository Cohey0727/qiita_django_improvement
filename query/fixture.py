import random
from tqdm import tqdm

from .models import *

GROUP_COUNT = 10000
USER_COUNT_BY_GROUP = 100
INVOICE_COUNT_BY_USER = 10
BATCH_SIZE = 500


def run():
    # create groups
    groups = [Group(name=f'group-{index}') for index in range(GROUP_COUNT)]
    Group.objects.bulk_create(groups, batch_size=BATCH_SIZE)

    # create users
    all_groups = Group.objects.all()
    users = [
        User(name=f'group-{group.id}_user-{index}', group=group)
        for index in range(USER_COUNT_BY_GROUP) for group in all_groups
    ]
    User.objects.bulk_create(users, batch_size=BATCH_SIZE)

    # create invoices
    all_users = User.objects.all()
    invoices = []
    for user in tqdm(all_users):
        invoices.extend([
            Invoice(price=random.randint(1000, 100000), user=user)
            for index in range(INVOICE_COUNT_BY_USER)
        ])
        if len(invoices) >= BATCH_SIZE:
            Invoice.objects.bulk_create(invoices, batch_size=BATCH_SIZE)

            invoices = []

    Invoice.objects.bulk_create(invoices, batch_size=BATCH_SIZE)
