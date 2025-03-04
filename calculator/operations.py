from decimal import Decimal
from calculator.logger import logger  # Import logger

def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        logger.error("Attempted to divide by zero")
        raise ValueError("Cannot divide by zero")
    return a / b
