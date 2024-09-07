from dataclasses import dataclass, asdict
from typing import Any

from app.domain.database.user_entity import UserEntity


@dataclass(frozen=True)
class UserMessageDTO:
    """Message DTO"""

    user: UserEntity
    message: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "user": self.user.as_dict(),
            "message": self.message
        }
