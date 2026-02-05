"""This module serves as the entry point for the program."""
from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver
from balance.balance_observer import PrintObserver
from transaction.transaction_factory import TransactionFactory
from transaction.transaction_adapter import TransactionAdapter
from transaction.external_income_transaction import ExternalFreelanceIncome


def main():
    print("Adding transactions...")
   
    # 1. Create balance (Singleton) and add observers
    balance = Balance.get_instance()
    print_observer = PrintObserver()
    low_balance_alert = LowBalanceAlertObserver(threshold=50)
    balance.register_observer(print_observer)
    balance.register_observer(low_balance_alert)

    # Create standard transactions
    # Use the Factory Method to create transactions
    transactions = [
        TransactionFactory.create_transaction(100, "INCOME"),
        TransactionFactory.create_transaction(60, "EXPENSE"),
        TransactionFactory.create_transaction(200, "INCOME"),
        TransactionFactory.create_transaction(90, "EXPENSE"),
    ]

    # Create an external income transaction (via Adapter pattern)
    freelance_income = ExternalFreelanceIncome(1200, "INV-98765", "Mobile App Project")
    adapter = TransactionAdapter(freelance_income)
    adapted_transaction = adapter.to_transaction()

    all_transactions = transactions + [adapted_transaction]

    # 2. Apply all transactions to balance
    for t in all_transactions:
        balance.apply_transaction(t)

    print("\nFinal Summary:")
    print(balance.summary())

if __name__ == "__main__":
    main()
