"""
Example implementation of a notification system using the factory design pattern
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING

from notification_factory import NotifierChannel, NotifierRegistry

if TYPE_CHECKING:
    from notifiers import Notifier


@dataclass
class Notification:
    """Represents a notification to be sent"""

    user_id: int
    message: str
    title: str


def main() -> None:
    """Script for example notification system"""

    my_notification = Notification(
        user_id=1234,
        message="Test message",
        title="Test title",
    )

    print(f"Sending notification to user ID: {my_notification.user_id}")

    email_notifier: Notifier = NotifierRegistry().get_notifier(
        NotifierChannel.EMAIL,
    )
    email_notifier.send(
        my_notification.user_id, my_notification.message, my_notification.title
    )

    sms_notifier: Notifier = NotifierRegistry().get_notifier(
        NotifierChannel.SMS,
    )
    sms_notifier.send(
        my_notification.user_id, my_notification.message, my_notification.title
    )


if __name__ == "__main__":
    main()
