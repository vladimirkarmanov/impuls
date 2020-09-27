from django.contrib.auth.models import Group

from register.models import User


class UserService:
    @staticmethod
    def activate_user_accout_after_email_confirmation(user) -> None:
        """Активация аккаунта после перехода по ссылке из email"""
        user.is_active = True
        user.email_confirmed = True
        password = User.objects.make_random_password()
        user.set_password(password)
        user.email_user(subject='Доступ к аккаунту',
                        message=f'Ваш пароль: {password}')
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
