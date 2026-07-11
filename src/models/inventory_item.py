from peewee import (BooleanField, CharField, DecimalField, IntegerField,
                    TextField)

from .base import BaseModelExtended, TimestampMixin


class InventoryItem(BaseModelExtended, TimestampMixin):
    """Inventory item model"""
    sku = CharField(max_length=50, unique=True, index=True)
    name = CharField(max_length=100, index=True)
    description = TextField(null=True)
    category = CharField(max_length=50, index=True)
    unit_price = DecimalField(max_digits=10, decimal_places=2)
    cost_price = DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = IntegerField(default=0)
    reorder_level = IntegerField(default=0)
    is_active = BooleanField(default=True)

    class Meta:
        table_name = 'inventory_items'
        indexes = (
            (('sku', 'name'), False),
        )

    def __str__(self):
        return f"{self.sku} - {self.name}"

    @property
    def in_stock(self) -> bool:
        """Check if item is in stock"""
        return self.stock_quantity > 0

    @property
    def needs_reorder(self) -> bool:
        """Check if item needs reordering"""
        return self.stock_quantity <= self.reorder_level
