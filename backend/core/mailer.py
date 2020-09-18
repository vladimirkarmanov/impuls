from django.core import mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class Mailer:
    """
    Send email messages helper class
    """

    def __init__(self, from_email='impuls@mail.ru'):
        # TODO setup the default from email
        self.connection = mail.get_connection()
        self.from_email = from_email

    def send_messages(self, subject, template, context, to_emails):
        messages = self.__generate_messages(subject, template, context, to_emails)
        self.__send_mail(messages)

    def __send_mail(self, mail_messages):
        self.connection.open()
        self.connection.send_messages(mail_messages)
        self.connection.close()

    def __generate_messages(self, subject, template, context, to_emails):
        messages = []
        for recipient in to_emails:
            message = EmailMessage(subject,
                                   render_to_string(template, context),
                                   to=[recipient],
                                   from_email=self.from_email)
            message.content_subtype = 'html'
            messages.append(message)

        return messages
