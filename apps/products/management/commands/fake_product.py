from itertools import cycle
from random import sample

from django.core.management import BaseCommand
from faker import Faker
from model_bakery import baker


class Command(BaseCommand):
    fake = Faker()

    def add_arguments(self, parser):
        parser.add_argument('-p', '--product', type=int, help='Define a product count', )
        parser.add_argument('-c', '--category', type=int, help='Define a category count', )

    def handle(self, *args, **options):
        if c := options.get('category', 20):
            baker.make(
                'products.Category',
                title=cycle(self.fake.sentences(nb=50)),
                _quantity=c,
            )
        if p := options.get('product', 20):
            baker.make(
                'products.Product',
                title=cycle(self.fake.sentences(nb=50)),
                description=cycle(self.fake.texts(nb_texts=5, max_nb_chars=100)),
                quantity=cycle(range(10, 90)),
                price=cycle(sample(range(10, 90), 10)),
                _quantity=p,
                make_m2m=True
            )
