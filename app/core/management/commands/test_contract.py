from django.core.management.base import BaseCommand
from core.models import CreditApplication, Contract


class Command(BaseCommand):
    help = 'Fetch unique manufacturer IDs by contract number'

    def add_arguments(self, parser):
        parser.add_argument('--id', type=int, help='Contract number')

    def handle(self, *args, **kwargs):
        contract_number = kwargs['id']
        self.stdout.write(self.style.SUCCESS(f'Received contract_number: {contract_number}'))

        contract = Contract.objects.filter(contract_number=contract_number).first()
        if not contract:
            self.stdout.write(self.style.ERROR(f'Контракт с номером {contract_number} не найден.'))
            return

        self.stdout.write(self.style.SUCCESS(f'Found contract: {contract.contract_number}'))

        unique_manufacturer_ids = CreditApplication.get_unique_manufacturer_ids_by_contract(contract.id)
        self.stdout.write(self.style.SUCCESS(
            f'Уникальные ID производителей для контракта {contract_number}: {list(unique_manufacturer_ids)}'))
