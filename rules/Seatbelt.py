from rule import Rules
from models.observation import Observation
from models.violation import Violation
from typing import Optional


class Seatbelt_Rule(Rules):
    def __init__(self, fee: float):
        self.fee = fee
        self.name = "Seatbelt rule"

    def check(self, observation: Observation) -> Optional[Violation]:
        if not observation.seatbelt_fastened:
            return Violation("Seatbelt not fastned", self.fee)
        return None
