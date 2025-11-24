from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Teacher:
    id: str
    name: str
    created_at: Optional[datetime] = None
