from dataclasses import dataclass

from app.domain.gateways.message_dto import MessageDTO


@dataclass(frozen=True)
class SmsMessageDto(MessageDTO):
    phone: str
