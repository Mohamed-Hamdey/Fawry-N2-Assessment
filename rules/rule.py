from abc import ABC, abstractmethod
from models.observation import Observation
from models.violation import Violation
from typing import Optional


class Rules(ABC):     #Abstract class for farthur rues to make the sys more flexible to extend
    name : str = "Rule"
    @abstractmethod
    def check(self, observation: Observation) -> Optional[Violation]:
        raise NotImplementedError