from django.contrib.auth.models import Group

from core.mailer import Mailer
from register.models import User


class UserService:
    @staticmethod
    def activate_user_accout_after_email_confirmation(user) -> None:
        """Активация аккаунта после перехода по ссылке из email"""
        user.is_active = True
        user.email_confirmed = True
        password = User.objects.make_random_password()
        user.set_password(password)
        mailer = Mailer()
        mailer.send_messages(subject='Доступ к аккаунту',
                             text=f'Ваш пароль: {password}',
                             to_emails=[user.email])
        user.save()

    @staticmethod
    def add_user_to_group_listeners(user) -> None:
        """Добавление пользователя в группу слушателей"""
        group, created = Group.objects.get_or_create(name='Слушатели')
        group.user_set.add(user)
        group.save()

    @staticmethod
    def add_user_to_group_teachers(user) -> None:
        """Добавление пользователя в группу преподавателей"""
        group, created = Group.objects.get_or_create(name='Преподаватели')
        group.user_set.add(user)
        group.save()
