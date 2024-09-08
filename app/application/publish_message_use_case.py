from app.domain.exceptions.decorators.generic_error_handler import generic_error_handler
from app.domain.notifications.notification_dto import NotificationDTO
from app.domain.notifications.notification_service import NotificationService


class PublishMessageUseCase:
    def __init__(self, notification_service: NotificationService):
        self._notification_service = notification_service

    @generic_error_handler
    def publish(self, notification: NotificationDTO):
        self._notification_service.send(notification=notification)
