from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide
from calculator.logger import logger  

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
    
    @staticmethod    
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        try:
            result = self.operation(self.a, self.b)
            logger.info(f"Performed calculation: {self.a} {self.operation.__name__} {self.b} = {result}")
            return result
        except Exception as e:
            logger.error(f"Error in calculation: {self.a} {self.operation.__name__} {self.b} - {str(e)}")
            raise e  

    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"
