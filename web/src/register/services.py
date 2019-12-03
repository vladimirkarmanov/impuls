from django.contrib.auth.models import Group

from .models import User


def activate_user_accout_after_email_confirm(user):
    user.is_active = True
    user.email_confirmed = True
    password = User.objects.make_random_password()
    user.set_password(password)
    user.email_user(subject='Доступ к аккаунту',
                    message=f'Ваш пароль: {password}')
    user.save()


def add_user_to_group_listeners(user):
    group, created = Group.objects.get_or_create(name='Слушатели')
    group.user_set.add(user)
    group.save()
