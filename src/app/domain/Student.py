from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class Evaluation:
    name: str
    score: float
    weight: float

@dataclass
class Student:
    id: str
    evaluations: List[Evaluation] = field(default_factory=list)
    attendance_ok: bool = True
    extra_points: float = 0.0
