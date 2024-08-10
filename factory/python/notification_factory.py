"""Module for configuration of notification system"""

from __future__ import annotations
from enum import auto, IntEnum
from typing import Type, TYPE_CHECKING

from notifiers import EmailNotifier, SmsNotifier

if TYPE_CHECKING:
    from notifiers import Notifier


class NotifierChannel(IntEnum):
    """Enumeration of available notification types"""

    EMAIL = auto()
    SMS = auto()


class NotificationChannelInvalidError(Exception):
    """Raised when attempting to retreive the notification class for an unknown channel"""


class NotifierRegistry:
    """Registry for mapping notification types to their concrete implementations"""

    def __init__(self) -> None:
        self._notifier_types: dict[NotifierChannel, Type[Notifier]] = (
            self.__register_default_notifiers()
        )

    def __register_default_notifiers(
        self,
    ) -> dict[NotifierChannel, Type[Notifier]]:
        """
        Registers the default notification types
        """
        return {
            NotifierChannel.EMAIL: EmailNotifier,
            NotifierChannel.SMS: SmsNotifier,
        }

    def register_notifier(
        self,
        notification_channel: NotifierChannel,
        notification_class: Type[Notifier],
    ) -> None:
        """Adds a notification type to the registry of available notification
        channels if it doesn't already exist

        :param notification_channel: Notification channel key
        :param notification_class: Implementation class for the channel key
        """
        self._notifier_types.setdefault(notification_channel, notification_class)

    def get_notifier(self, notification_channel: NotifierChannel) -> Notifier:
        """Returns an instance of the notification class for the specified channel

        :param notification_channel: Notification channel key
        """
        notification_class = self._notifier_types.get(notification_channel)
        if notification_class is None:
            raise NotificationChannelInvalidError(
                f"Notification channel '{notification_channel}' not found."
            )
        return notification_class()
