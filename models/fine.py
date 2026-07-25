from typing import List
from violation import Violation

class Fine:
    def __init__(self,plate_number: str, Violations: List[Violation]):
        self.plate_number = plate_number
        self.violations = Violations
    
    def total_fees(self) -> float:
        return sum( v.fee for v in self.violations)
    
    def print_fine(self) -> None:
        print(f"Traffic for car {self.plate_number}")
        print(f"Total amount: {self.total_amount}")
        print("Violations:")
        for v in self.violations:
            print(f"- {v.description} : {v.fee}")