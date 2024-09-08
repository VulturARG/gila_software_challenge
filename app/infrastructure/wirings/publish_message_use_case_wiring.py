from app.application.publish_message_use_case import PublishMessageUseCase
from app.domain.database.database_repository import DatabaseRepository
from app.domain.gateways.email_port import EmailPort
from app.domain.gateways.file_port import FilePort
from app.domain.gateways.push_notification_port import PushNotificationPort
from app.domain.gateways.sms_port import SmsPort
from app.domain.logs.log_port import LogPort
from app.domain.logs.log_service import LogService
from app.domain.notifications.notification_service import NotificationService
from app.infrastructure.adapters.database.user_adapter import UsersAdapter
from app.infrastructure.adapters.gateway.email_adapter import EmailAdapter
from app.infrastructure.adapters.gateway.file_gateway_adapter import FileGatewayAdapter
from app.infrastructure.adapters.gateway.push_notification_adapter import (
    PushNotificationAdapter,
)
from app.infrastructure.adapters.gateway.sms_adapter import SmsAdapter
from app.infrastructure.logs.log_adapter import LogAdapter
from app.infrastructure.tests.test_doubles.mock_orm import MockORM


class PublishMessageUseCaseWiring:
    def instantiate(self) -> PublishMessageUseCase:
        return PublishMessageUseCase(
            notification_service=self._notification_service(),
        )

    def _notification_service(self) -> NotificationService:
        return NotificationService(
            email_port=self._email_port(),
            sms_port=self._sms_port(),
            push_notification_port=self._push_notification_port(),
            user_repository=self._user_repository(),
        )

    def _log_service(self) -> LogService:
        return LogService(log_port=self._log_port())

    def _email_port(self) -> EmailPort:
        return EmailAdapter(
            log_service=self._log_service(),
        )

    def _sms_port(self) -> SmsPort:
        return SmsAdapter(
            log_service=self._log_service(),
        )

    def _push_notification_port(self) -> PushNotificationPort:
        return PushNotificationAdapter(
            log_service=self._log_service(),
        )

    def _user_repository(self) -> DatabaseRepository:
        return UsersAdapter(orm=MockORM())

    def _log_port(self) -> LogPort:
        return LogAdapter(
            file_port=self._file_port(),
            file_path="logs/log.txt",
        )

    def _file_port(self) -> FilePort:
        return FileGatewayAdapter()
