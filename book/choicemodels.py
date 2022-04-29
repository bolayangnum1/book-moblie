from django.contrib.auth import get_user_model


User = get_user_model()

BOOK_TYPE = (
    ('1', 'Бесплатно'),
    ('2', 'Премиум'),
)