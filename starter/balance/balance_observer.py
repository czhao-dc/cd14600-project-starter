# balance_observer.py

class IBalanceObserver:
    def update(self, balance, transaction):
        """Handle balance updates."""
        raise NotImplementedError("Subclasses must implement update method.")


class PrintObserver(IBalanceObserver):
    def update(self, balance, transaction):
        """Print balance update message."""
        print(f"Transaction Applied: {transaction}")
        print(balance.summary())
        print("-" * 20)


class LowBalanceAlertObserver(IBalanceObserver):
    def __init__(self, threshold):
        self.threshold = threshold
        self.alert_triggered = False

    def update(self, balance, transaction):
        """Alert if balance drops below threshold."""
        if balance.get_balance() < self.threshold:
            self.alert_triggered = True
            print(f"ALERT: Balance is below ${self.threshold}! Current balance: ${balance.get_balance():.2f}")
        else:
            self.alert_triggered = False
