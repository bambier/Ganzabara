from utils.logger import get_logger

# Database core
from .account import Account
# Base utilities
from .base import BaseModelExtended, SoftDeleteMixin, TimestampMixin
from .customer import Customer
from .database import BaseModel, _db, db_manager, init_database
from .employee import Employee
from .inventory_item import InventoryItem
from .invoice import Invoice
from .sales import Billing, Sale, SaleItem
from .transaction import Transaction
from .user import User

# All models

logger = get_logger()

# List all models for table creation
ALL_MODELS = [
    User,
    Account,
    Employee,
    Customer,
    InventoryItem,
    Sale,
    SaleItem,
    Invoice,
    Transaction,
    Billing
]


def create_tables() -> None:
    """Create all tables if they don't exist"""
    _db.create_tables(ALL_MODELS, safe=True)


def drop_tables() -> None:
    """Drop all tables (use with caution)"""
    _db.drop_tables(ALL_MODELS, safe=True)


def initialize_test_data() -> None:
    """Initialize test data for development"""
    if User.select().count() == 0:
        # Create admin user
        admin = User.create(
            username='admin',
            email='admin@example.com',
            password_hash='hashed_password',
            is_admin=True,
            is_active=True
        )

        # Create sample customer
        customer = Customer.create(
            name='John Doe',
            email='john@example.com',
            phone='123-456-7890',
            address='123 Main St',
            city='New York',
            state='NY',
            country='USA',
            postal_code='10001',
            created_by=admin
        )

        logger.info("Test data created successfully!")


# What to export
__all__ = [
    # Database
    'BaseModel',
    'init_database',
    'db_manager',
    '_db',

    # Base utilities
    'BaseModelExtended',
    'TimestampMixin',
    'SoftDeleteMixin',

    # Models
    'User',
    'Account',
    'Employee',
    'Customer',
    'InventoryItem',
    'Sale',
    'SaleItem',
    'Invoice',
    'Transaction',
    'Billing',

    # Utilities
    'ALL_MODELS',
    'create_tables',
    'drop_tables',
    'initialize_test_data'
]
