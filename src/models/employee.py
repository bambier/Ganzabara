from peewee import (BooleanField, CharField, DateField, DecimalField,
                    ForeignKeyField)

from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .user import User


class Employee(BaseModelExtended, TimestampMixin, SoftDeleteMixin):
    """Employee model"""
    user = ForeignKeyField(User, backref='employee', unique=True)
    employee_id = CharField(max_length=20, unique=True, index=True)
    department = CharField(max_length=50)
    position = CharField(max_length=50)
    hire_date = DateField()
    salary = DecimalField(max_digits=10, decimal_places=2)
    is_active = BooleanField(default=True)

    class Meta:
        table_name = 'employees'

    def __str__(self):
        return f"{self.employee_id} - {self.position}"
