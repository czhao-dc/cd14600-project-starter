# balance.py

from transaction.transaction_category import TransactionCategory

class Balance:
    """Singleton to track the balance."""

    _instance = None

    @classmethod
    def get_instance(cls):
        """Get the singleton instance of the Balance class."""
        if cls._instance is None:
            cls._instance = Balance()
        return cls._instance

    def __init__(self):
        """Initialize the balance. Prevent direct instantiation."""
        if Balance._instance is not None:
            raise RuntimeError("This class is a singleton! Use get_instance() to get the instance.")
        self._balance = 0.0
        self._observers = []

    def reset(self):
        """Reset the net balance to zero."""
        self._balance = 0.0
        # Optionally, you might want to clear observers on reset as well
        # self._observers = []

    def add_income(self, amount):
        """Add income to the balance."""
        self._balance += amount

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        self._balance -= amount

    def apply_transaction(self, transaction):
        """
        Apply a Transaction object to update the balance.
        
        Args:
            transaction (Transaction): The transaction to apply.
        
        Raises:
            ValueError: If the transaction category is invalid.
        """
        if transaction.category == TransactionCategory.INCOME:
            self.add_income(transaction.amount)
        elif transaction.category == TransactionCategory.EXPENSE:
            self.add_expense(transaction.amount)
        else:
            raise ValueError("Invalid transaction category")
        self.notify_observers(transaction)

    def get_balance(self):
        """Get the current net balance."""
        return self._balance

    def summary(self):
        """Return a summary string of the net balance."""
        return f"Current Balance: ${self.get_balance():.2f}"

    def register_observer(self, observer):
        """Register an observer to be notified of balance changes."""
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister_observer(self, observer):
        """Unregister an observer."""
        self._observers.remove(observer)

    def notify_observers(self, transaction):
        """Notify all registered observers of a balance change."""
        for observer in self._observers:
            observer.update(self, transaction)
