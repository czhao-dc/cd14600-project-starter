# transaction/test_transaction_factory.py

import unittest
from transaction.transaction_factory import TransactionFactory
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory

class TestTransactionFactory(unittest.TestCase):

    def test_create_income_transaction(self):
        """Test creating an income transaction."""
        transaction = TransactionFactory.create_transaction(150.0, "INCOME")
        self.assertIsInstance(transaction, Transaction)
        self.assertEqual(transaction.amount, 150.0)
        self.assertEqual(transaction.category, TransactionCategory.INCOME)

    def test_create_expense_transaction(self):
        """Test creating an expense transaction."""
        transaction = TransactionFactory.create_transaction(75.50, "EXPENSE")
        self.assertIsInstance(transaction, Transaction)
        self.assertEqual(transaction.amount, 75.50)
        self.assertEqual(transaction.category, TransactionCategory.EXPENSE)