from rules.rule import Rules
from models.fine import Fine
from models.violation import Violation
from models.observation import Observation
from typing import Optional,List,Dict



class Qu_Radar:
    
    def __init__(self):
        self.rules: List[Rules] = []
        self.fines: List[Fine] = []
        self.violation_counts: Dict[str, int] = {}
    
    def add_Rule(self, rule: Rules) -> None:
        self.rules.append(rule)
        
    def Radar_Process(self, observation: Observation) -> Optional[Fine]:
        violations: List[Violation] = []
        
        for rule in self.rules:
            vio= rule.check(observation)
            if vio is not None:
                violations.append(vio)
                self.violation_counts[rule.name] = self.violation_counts.get(rule.name,0) + 1 
                
        if not violations:
            return None          
        
        fine = Fine(observation.plate_number, violations)
        self.fines.append(fine)
        return fine
    def get_All_Fines(self) -> List[Dict[str, float]]:
        return [
            {"plate_number": fine.plate_number, "total_amount": fine.total_amount}
            for fine in self.fines
        ]
    
    def get_all_violate_rules(self) -> Dict[str, int]:
        return dict(self.violation_counts)
