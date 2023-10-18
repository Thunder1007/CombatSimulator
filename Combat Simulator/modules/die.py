

import random

class die:
    def __init__(self, amount: int, size: int):
        
        self.amount = amount
        self.size = size

    def __str__(self) -> str:

        return f"{self.amount}d{self.size}"

    def rolls(self) ->  list[int]:
        
        rolls = []

        for i in range(self.amount):
            rolls.append(random.randint(1, self.size))
        
        return rolls



