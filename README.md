# currency-converter-python
Object-Oriented Currency Converter in Python using live API rates.

 # Features
OOP Architecture: Uses a base class (`Moneda`) and specific derived classes (`Euro`, `Dolar`, `Leu`).
Live API Integration: Fetches up-to-date daily exchange rates from an external JSON API using the `requests` library.
Offline Fallback: Includes error handling (`try-except`) with localized hardcoded backup rates to ensure the application remains functional even without an internet connection.
Input Validation: Prevents application crashes by validating user input types.

