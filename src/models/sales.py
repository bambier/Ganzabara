from datetime import datetime

from peewee import (CharField, DateTimeField, DecimalField, ForeignKeyField,
                    IntegerField, TextField)

from .base import BaseModelExtended, TimestampMixin
from .customer import Customer
from .inventory_item import InventoryItem
from .user import User


class Sale(BaseModelExtended, TimestampMixin):
    """Sales record"""
    id = IntegerField(primary_key=True)
    customer = ForeignKeyField(Customer, backref='sales')
    user = ForeignKeyField(User, backref='sales')
    sale_date = DateTimeField(default=datetime.now)
    total_amount = DecimalField(max_digits=10, decimal_places=2)
    discount = DecimalField(max_digits=5, decimal_places=2, default=0)
    tax_amount = DecimalField(max_digits=10, decimal_places=2, default=0)
    status = CharField(max_length=20, default='pending', index=True)
    # status: pending, completed, cancelled, refunded
    notes = TextField(null=True)

    class Meta:
        table_name = 'sales'

    def __str__(self):
        return f"Sale #{self.id} - {self.customer.name}"

    @property
    def net_amount(self) -> float:
        """Calculate net amount after discount and tax"""
        return float(self.total_amount - self.discount + self.tax_amount)


class SaleItem(BaseModelExtended):
    """Individual items in a sale"""
    sale = ForeignKeyField(Sale, backref='items')
    item = ForeignKeyField(InventoryItem, backref='sale_items')
    quantity = IntegerField()
    unit_price = DecimalField(max_digits=10, decimal_places=2)
    total_price = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        table_name = 'sale_items'

    def __str__(self):
        return f"{self.quantity}x {self.item.name} (Sale #{self.sale.id})"


class Billing(BaseModelExtended):
    """Billings"""
    name = CharField(max_length=50)
    price = DecimalField(max_digits=10, decimal_places=2)
    count = DecimalField(max_digits=10, decimal_places=2)
