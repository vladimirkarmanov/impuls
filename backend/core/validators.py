from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\d{6,11}$',
    message='Телефон должен быть в формате: 89991234567'
)

mail_index_regex = RegexValidator(
    regex=r'^\d{5,6}$',
    message='Почтовый индекс должен быть в формате: 123456'
)

only_russian_chars = RegexValidator(
    regex=r'[а-яё]|[А-ЯЁ]',
    message='Это поле может содержать только русские буквы'
)

only_numbers = RegexValidator(
    regex=r'^\d{0,9}$',
    message='Это поле должно содержать только цифры'
)
