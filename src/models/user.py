
from peewee import BooleanField, CharField, DateTimeField

from .base import BaseModelExtended, TimestampMixin


class User(BaseModelExtended, TimestampMixin):
    """User model for authentication"""
    username = CharField(max_length=50, unique=True, index=True)
    email = CharField(max_length=100, unique=True, index=True)
    password_hash = CharField(max_length=255)
    is_active = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    last_login = DateTimeField(null=True)

    class Meta:
        table_name = 'users'
        indexes = (
            (('username', 'email'), False),
        )

    def __str__(self):
        return self.username

    @classmethod
    def get_by_username(cls, username: str):
        """Get user by username"""
        return cls.get_or_none(username=username)

    @classmethod
    def get_by_email(cls, email: str):
        """Get user by email"""
        return cls.get_or_none(email=email)

    def is_authenticated(self) -> bool:
        """Check if user is authenticated"""
        return self.is_active
