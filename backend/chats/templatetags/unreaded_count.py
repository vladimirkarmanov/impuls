from django import template

register = template.Library()


@register.simple_tag
def unreaded_msg_count(user, chat):
    return chat.messages.exclude(author=user).unreaded().count()
