from app.domain.notifications.notification_category import NotificationCategory
from pydantic import BaseModel, Field, field_validator


class NotificationRequest(BaseModel):
    category: str = Field(...)
    message: str = Field(..., min_length=1)

    @field_validator("category")
    @classmethod
    def validate_category(cls, value: str) -> str:
        if value.lower() not in [category.value for category in NotificationCategory]:
            message = f"Invalid category. Must be one of: {', '.join([c.value for c in NotificationCategory])}"
            raise ValueError(message)
        return value.lower()
