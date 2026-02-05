# transaction_adapter.py

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory

class TransactionAdapter:
    def __init__(self, external_transaction):
        self.external_transaction = external_transaction

    def to_transaction(self):
        """Convert an external transaction to a standard Transaction."""
        # The external transaction's 'typ' is "income", so we map it to our INCOME category.
        if self.external_transaction.typ.lower() == "income":
            return Transaction(self.external_transaction.amount, TransactionCategory.INCOME)
        return None # Or handle other types if necessary
