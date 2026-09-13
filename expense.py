"""Expense model for the expense manager application."""

from dataclasses import dataclass
from typing import Any


@dataclass
class Expense:
    """Represents a single expense record."""

    title: str
    amount: float
    category: str

    def to_dict(self) -> dict[str, Any]:
        """Serialize the expense to a JSON-compatible dictionary."""
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Expense":
        """Create an Expense from a dictionary loaded from JSON."""
        return cls(
            title=str(data["title"]),
            amount=float(data["amount"]),
            category=str(data["category"]),
        )
