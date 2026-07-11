from datetime import datetime

from peewee import (CharField, DateTimeField, DecimalField, ForeignKeyField,
                    TextField)

from .base import BaseModelExtended, TimestampMixin
from .customer import Customer
from .sales import Sale
from .user import User


class Invoice(BaseModelExtended, TimestampMixin):
    """Invoice model"""
    sale = ForeignKeyField(Sale, backref='invoice', unique=True)
    customer = ForeignKeyField(Customer, backref='invoices')
    user = ForeignKeyField(User, backref='invoices')
    invoice_number = CharField(max_length=50, unique=True, index=True)
    invoice_date = DateTimeField(default=datetime.now)
    due_date = DateTimeField()
    subtotal = DecimalField(max_digits=10, decimal_places=2)
    tax = DecimalField(max_digits=10, decimal_places=2)
    discount = DecimalField(max_digits=10, decimal_places=2, default=0)
    total = DecimalField(max_digits=10, decimal_places=2)
    paid_amount = DecimalField(max_digits=10, decimal_places=2, default=0)
    status = CharField(max_length=20, default='pending', index=True)
    # status: draft, pending, paid, overdue, cancelled
    notes = TextField(null=True)

    class Meta:
        table_name = 'invoices'

    def __str__(self):
        return f"Invoice #{self.invoice_number}"

    @property
    def balance_due(self) -> float:
        """Calculate remaining balance"""
        return float(self.total - self.paid_amount)

    @property
    def is_paid(self) -> bool:
        """Check if invoice is fully paid"""
        return self.balance_due <= 0 and self.status == 'paid'
