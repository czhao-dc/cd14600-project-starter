# Personal Finance Manager — Design Patterns Project

This project is a hands-on exercise in applying Object-Oriented Design Patterns to build a simplified personal finance manager.
It implements and extends starter code to add functionality such as tracking transactions, adapting external data, observing balance changes, and ensuring proper architectural patterns.

## Getting Started

### Dependencies

Make sure you have Python version >= 3.8.x installed on your computer.


### Installation

1. Clone the repo:

```
bash
git clone https://github.com/udacity/cd14600-project-starter.git
cd cd14600-project-starter/starter
```

2. Run the Program: 
```
python main.py
```

## Testing

This project uses Python’s built-in unittest framework.

To run all tests:

```
python -m unittest discover
```

To run a single test file:
```
python -m unittest balance/test_balance_observer.py
```

### Break Down Tests

- test_balance.py → Verifies correct implementation of the Singleton Balance class.
- test_transaction.py → Confirms transactions update balances correctly.
- test_transaction_adapter.py → Ensures external income data is correctly adapted into Transaction objects.
- test_balance_observer.py → Validates that low-balance alerts are triggered at the correct threshold.

## Design Pattern Reflection
This project utilizes four key design patterns to create a modular, maintainable, and scalable application.

### 1. Singleton Pattern

*   **Implementation**: The `Balance` class is implemented as a Singleton. It has a private `_instance` variable and a public class method `get_instance()` that returns the single instance. The constructor will raise a `RuntimeError` if instantiated directly more than once.
*   **Rationale**: The application's balance should be a single, globally consistent value. The Singleton pattern guarantees that there is only one `Balance` object, preventing different parts of the application from creating separate, conflicting balance states. This provides a single source of truth for the user's financial status.
*   **Trade-offs**: While ensuring a single instance, Singletons can introduce global state, which can make unit testing more difficult. This was mitigated by adding a `reset()` method that is called in the `setUp()` of each test, ensuring tests run independently.

### 2. Adapter Pattern

*   **Implementation**: The `TransactionAdapter` class takes an `ExternalFreelanceIncome` object (which has a different structure and naming convention) and converts it into a standard `Transaction` object that the rest of our application can understand.
*   **Rationale**: This pattern was chosen to allow our application to work with incompatible, third-party data sources without modifying our core internal classes. It acts as a translator, promoting code reuse and decoupling our system from external dependencies. If the external API changes, we only need to update the adapter, not our core logic.
*   **Trade-offs**: For every new external data type, a new adapter class must be created. In a system with many different external integrations, this could lead to a large number of adapter classes to maintain.

### 3. Observer Pattern

*   **Implementation**: The `Balance` class acts as the "Subject" (or "Observable"). It maintains a list of "Observers" (`PrintObserver`, `LowBalanceAlertObserver`). When the balance changes via `apply_transaction()`, it calls the `notify_observers()` method, which in turn calls the `update()` method on each registered observer.
*   **Rationale**: This pattern creates a clean separation between the data (`Balance`) and the components that react to changes in that data (the observers). It allows us to add new notification behaviors (e.g., sending an email, logging to a file) simply by creating a new observer class, without ever modifying the `Balance` class. This makes the system highly extensible and follows the Open/Closed Principle.
*   **Trade-offs**: The flow of control can be less obvious, which can make debugging more complex, especially if observers trigger other updates. In complex scenarios, it can lead to unexpected cascades of updates.

### 4. Factory Method Pattern (Student's Choice)

*   **Implementation**: The `TransactionFactory` provides a static method `create_transaction()` that abstracts the creation of `Transaction` objects. Instead of calling the `Transaction` constructor directly with a `TransactionCategory` enum, the client code (`main.py`) calls the factory with a simple string ("INCOME" or "EXPENSE").
*   **Rationale**: The Factory Method was chosen to decouple the client code from the concrete implementation of transaction creation. This simplifies the creation process for the client and centralizes the instantiation logic. If we were to introduce different transaction subclasses in the future (e.g., `RecurringExpense`, `InvestmentIncome`), we would only need to update the factory, and the client code would remain unchanged.
*   **Trade-offs**: For a simple object like `Transaction`, a factory might seem like slight over-engineering. It adds an extra layer of abstraction and an additional class to the project. However, it pays off by making the system more scalable and easier to refactor as complexity grows.

## Project Instructions

1. Implement Singleton Balance Class – Ensure only one balance object exists throughout the app.
2. Complete Transaction Class – Handle income and expense transactions.
3. Implement Adapter Pattern – Adapt external freelance income data into internal Transaction objects.
4. Implement Observer Pattern – Create a low balance observer that triggers an alert when funds drop too low.
5. Add Unit Tests – Write tests for all implemented functionality.
6. Choose and Implement a Fourth Pattern – Pick one additional design pattern (e.g., Strategy, Command, Decorator, etc.) and integrate it into your project.
7. Provide a Reflection – Add a short write-up in your repo (README or separate file) explaining your design choices.

## Built With

* [Python](https://www.python.org/) – Main programming language
* [unittest](https://docs.python.org/3/library/unittest.html) – Testing framework
* [PEP8](https://peps.python.org/pep-0008/) – Style guide for Python code

## License

[License](LICENSE.txt)
