from django.db import models
from .mixins import UUIDMixin, TimeStampedMixin
from django.utils.translation import gettext_lazy as _


class Manufacturer(UUIDMixin, TimeStampedMixin):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "manufacturer"
        verbose_name = _('Manufacturer')
        verbose_name_plural = _('Manufacturers')


class Product(UUIDMixin, TimeStampedMixin):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Contract(UUIDMixin, TimeStampedMixin):
    contract_number = models.CharField(max_length=50)

    def __str__(self):
        return self.contract_number

    class Meta:
        db_table = "contract"
        verbose_name = _('Contract')
        verbose_name_plural = _('Contract')


class CreditApplication(UUIDMixin, TimeStampedMixin):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name='credit_application')
    products = models.ManyToManyField(Product, related_name='credit_applications')

    def __str__(self):
        return f'Credit Application for Contract {self.contract.contract_number}'

    class Meta:
        db_table = "credit_application"
        verbose_name = _('CreditApplication')
        verbose_name_plural = _('CreditApplications')

    @staticmethod
    def get_unique_manufacturer_ids_by_contract(contract_id):
        manufacturer_ids = Manufacturer.objects.filter(
            products__credit_applications__contract__id=contract_id
        ).distinct().values_list('id', flat=True)

        return manufacturer_ids
