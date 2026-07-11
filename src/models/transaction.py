from datetime import datetime

from peewee import (CharField, DateTimeField, DecimalField, ForeignKeyField,
                    TextField)

from .base import BaseModelExtended, TimestampMixin
from .customer import Customer
from .invoice import Invoice
from .user import User


class Transaction(BaseModelExtended, TimestampMixin):
    """Payment transaction model"""
    invoice = ForeignKeyField(Invoice, backref='transactions', null=True)
    customer = ForeignKeyField(Customer, backref='transactions')
    user = ForeignKeyField(User, backref='transactions')
    transaction_id = CharField(max_length=100, unique=True, index=True)
    amount = DecimalField(max_digits=10, decimal_places=2)
    payment_method = CharField(max_length=50, index=True)
    # payment_method: cash, credit_card, bank_transfer, cheque, online
    payment_date = DateTimeField(default=datetime.now)
    status = CharField(max_length=20, default='pending', index=True)
    # status: pending, completed, failed, refunded
    reference = CharField(max_length=100, null=True)
    notes = TextField(null=True)

    class Meta:
        table_name = 'transactions'
        indexes = (
            (('transaction_id', 'payment_method'), False),
        )

    def __str__(self):
        return f"Transaction {self.transaction_id} - ${self.amount}"

    @classmethod
    def get_by_transaction_id(cls, transaction_id: str):
        """Get transaction by transaction ID"""
        return cls.get_or_none(transaction_id=transaction_id)
