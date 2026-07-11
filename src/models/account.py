from peewee import CharField, ForeignKeyField, TextField

from .base import BaseModelExtended, TimestampMixin
from .database import BaseModel
from .user import User


class Account(BaseModelExtended, TimestampMixin):
    """User account/profile"""
    user = ForeignKeyField(User, backref='account', unique=True)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    phone = CharField(max_length=20, null=True)
    address = TextField(null=True)
    city = CharField(max_length=50, null=True)
    state = CharField(max_length=50, null=True)
    country = CharField(max_length=50, null=True)
    postal_code = CharField(max_length=20, null=True)

    class Meta:
        table_name = 'accounts'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self) -> str:
        """Get full name"""
        return f"{self.first_name} {self.last_name}"
