from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\d{6,11}$',
    message='Телефон должен быть в формате: 12345678910'
)

mail_index_regex = RegexValidator(
    regex=r'^\d{5,6}$',
    message='Почтовый индекс должен быть в формате: 123456'
)