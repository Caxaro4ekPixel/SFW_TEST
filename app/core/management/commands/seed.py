from django.core.management.base import BaseCommand
from core.models import Manufacturer, Product, Contract, CreditApplication
import uuid


class Command(BaseCommand):
    help = 'Seeds the database with test data'

    def handle(self, *args, **kwargs):
        manufacturer1 = Manufacturer.objects.create(id=uuid.uuid4(), name="Производитель 1")
        manufacturer2 = Manufacturer.objects.create(id=uuid.uuid4(), name="Производитель 2")
        manufacturer3 = Manufacturer.objects.create(id=uuid.uuid4(), name="Производитель 3")

        product1 = Product.objects.create(id=uuid.uuid4(), name="Товар 1", manufacturer=manufacturer1)
        product2 = Product.objects.create(id=uuid.uuid4(), name="Товар 2", manufacturer=manufacturer2)
        product3 = Product.objects.create(id=uuid.uuid4(), name="Товар 3", manufacturer=manufacturer3)

        contract1 = Contract.objects.create(id=uuid.uuid4(), contract_number="32812")
        contract2 = Contract.objects.create(id=uuid.uuid4(), contract_number="32813")

        credit_application1 = CreditApplication.objects.create(id=uuid.uuid4(), contract=contract1)
        credit_application1.products.add(product1, product2)

        credit_application2 = CreditApplication.objects.create(id=uuid.uuid4(), contract=contract2)
        credit_application2.products.add(product3)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))
