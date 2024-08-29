from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class MessageDTO(ABC):
    """Message DTO"""

    message: str
