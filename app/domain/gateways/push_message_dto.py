from dataclasses import dataclass

from app.domain.gateways.message_dto import MessageDTO


@dataclass(frozen=True)
class PushMessageDto(MessageDTO):
    push_id: str
