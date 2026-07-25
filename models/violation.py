from dataclasses import dataclass

@dataclass
class Violation:
    description : str
    fees: float
    