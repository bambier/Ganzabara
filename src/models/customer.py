from peewee import CharField, ForeignKeyField, TextField

from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .user import User


class Customer(BaseModelExtended, TimestampMixin, SoftDeleteMixin):
    """Customer model"""
    name = CharField(max_length=100, index=True)
    email = CharField(max_length=100, unique=True, index=True)
    phone = CharField(max_length=20)
    address = TextField()
    city = CharField(max_length=50)
    state = CharField(max_length=50)
    country = CharField(max_length=50)
    postal_code = CharField(max_length=20)
    created_by = ForeignKeyField(User, backref='customers', null=True)

    class Meta:
        table_name = 'customers'
        indexes = (
            (('name', 'email'), False),
        )

    def __str__(self):
        return self.name
