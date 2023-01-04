from enum import Enum, auto


class AssessmentStatus(Enum):
    DEFAULT = auto()
    COMPLETED = auto()
    PENDING = auto()
    BLOCKED = auto()
    FAILED = auto()
    PASSED = auto()
