"""Example implementation of a notification system using the factory design pattern"""

from abc import ABCMeta, abstractmethod


class Notifier(metaclass=ABCMeta):
    """Abstract class for notifications"""

    @abstractmethod
    def send(self, user: int, message: str, title: str) -> None:
        """Sends a notification to the specified user.

        :param user: ID of the user to notify
        :param message: Notification content
        :param title: Header or title for the notificiation
        """


class EmailNotifier(Notifier):
    """Concrete implementation of an Email notifier"""

    def send(self, user: int, message: str, title: str) -> None:
        """Sends an email notification to the specified user.

        :param user: ID of the user to notify
        :param message: Email body
        :param title: Email subject line
        """
        print(f"Sending email to user ID: {user}. Subject: {title}, Body: {message}")


class SmsNotifier(Notifier):
    """Concrete implementation of a SMS notifier"""

    def send(self, user: int, message: str, title: str = "") -> None:
        """Sends an SMS notification to the specified user

        :param user: ID of the user to notify
        :param message: Text message content
        :param title: If specified, prepends message with title
        """
        content: str = f"{title}: {message}" if title else message
        print(f"Sending text message to user ID: {user}. {content}")
