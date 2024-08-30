from dataclasses import dataclass

from app.domain.database.user_entity import UserEntity


@dataclass(frozen=True)
class UserMessageDTO:
    """Message DTO"""

    user: UserEntity
    message: str
