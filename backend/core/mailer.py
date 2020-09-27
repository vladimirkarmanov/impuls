from typing import List

from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class Mailer:
    """
    Класс для отправки почты
    """

    def __init__(self, from_email='impuls@mail.ru'):
        # TODO setup the default from email
        self.connection = mail.get_connection()
        self.from_email = from_email

    def send_messages(self, subject, to_emails, text=None, template=None, context=None) -> None:
        messages = self._generate_messages(subject, to_emails, text, template, context)
        self._send_mail(messages)

    def _send_mail(self, mail_messages) -> None:
        self.connection.open()
        self.connection.send_messages(mail_messages)
        self.connection.close()

    def _generate_template_message(self, subject, template, context, recipient) -> EmailMessage:
        message = EmailMessage(subject,
                               render_to_string(template, context),
                               to=[recipient],
                               from_email=self.from_email)
        message.content_subtype = 'html'
        return message

    def _generate_plain_message(self, subject, text, recipient) -> EmailMessage:
        return EmailMessage(subject,
                            text,
                            to=[recipient],
                            from_email=self.from_email)

    def _generate_messages(self, subject, to_emails, text, template, context) -> List[EmailMessage]:
        messages = []
        if template and context:
            messages = [self._generate_template_message(subject, template, context, recipient) for recipient in to_emails]
        elif text:
            messages = [self._generate_plain_message(subject, text, recipient) for recipient in to_emails]
        return messages
