from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def start_with_a_letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError(
            'Your name must start with a letter!'
        )


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError(
                'Fruit name should contain only letters!'
            )


class Profile(models.Model):
    MAX_LEN_FIRST_NAME = 25
    MIN_LEN_FIRST_NAME = 2

    MAX_LEN_LAST_NAME = 35
    MIN_LEN_LAST_NAME = 1

    MAX_LEN_EMAIL = 40

    MAX_LEN_PASSWORD = 20
    MIN_LEN_PASSWORD = 8

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_FIRST_NAME),
            start_with_a_letter_validator,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_LAST_NAME),
            start_with_a_letter_validator,
        ),
    )

    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
    )

    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        validators=(
            MinLengthValidator(MIN_LEN_PASSWORD),
        ),
    )

    image_url = models.URLField(
        blank=True, null=True,
    )

    age = models.PositiveIntegerField(
        blank=True, null=True,
        default=18,
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Fruit(models.Model):
    MAX_LEN_FRUIT_NAME = 30
    MIN_LEN_FRUIT_NAME = 2

    name = models.CharField(
        max_length=MAX_LEN_FRUIT_NAME,
        validators=(
            MinLengthValidator(MIN_LEN_FRUIT_NAME),
            only_letters_validator,
        ),
    )

    image_url = models.URLField(
    )

    description = models.TextField(
    )

    nutrition = models.TextField(
    )
