from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp) -> str:
        return (
                six.text_type(user.id) + six.text_type(timestamp) +
                six.text_type(user.email_confirmed)
        )


account_activation_token = AccountActivationTokenGenerator()
