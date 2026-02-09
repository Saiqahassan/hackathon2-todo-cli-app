from dataclasses import dataclass, field

@dataclass
class Task:
    id: int
    description: str
    completed: bool = False

    def __post_init__(self):
        if not self.description:
            raise ValueError("Task description cannot be empty.")
