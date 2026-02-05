# transaction/transaction_factory.py

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory

class TransactionFactory:
    """A factory for creating Transaction objects."""

    @staticmethod
    def create_transaction(amount: float, category_str: str) -> Transaction:
        """
        Creates a Transaction object from a string category.

        Args:
            amount (float): The transaction amount.
            category_str (str): The category as a string (e.g., "INCOME" or "EXPENSE").
        """
        category = TransactionCategory[category_str.upper()]
        return Transaction(amount, category)