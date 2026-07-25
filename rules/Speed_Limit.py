from rule import Rules
from models.observation import Observation
from models.violation import Violation
from typing import Optional



class Speed_Limit(Rules):
    def __init__(self, car_type: str, max_speed: float, fees: float):
        self.car_type = car_type
        self.max_speed = max_speed
        self.fees = fees
        self.name = f"{car_type} speed limit ({max_speed})"
        
    def check(self, observation: Observation) -> Optional[Violation]:
        if observation.car_type == self.car_type and observation.speed > self.max_speed:
            description = (f"speed of {observation.speed} exceeded max allowed speed ({self.max_speed})")
            return Violation(description,self.fees)
        return None