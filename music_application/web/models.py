from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from music_application.web.validators import validate_sting_alphanumeric


class Profile(models.Model):
    MIN_USERNAME_LEN = 2
    MAX_USERNAME_LEN = 15
    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=(
            MinLengthValidator(2),
            validate_sting_alphanumeric,
        ),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    MAX_ALBUM_NAME = 30
    MAX_ARTIST_NAME = 30
    MAX_GENRE_NAME = 30
    MIN_PRICE = 0.0

    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RNB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    OTHER_MUSIC = 'Other'

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    name = models.CharField(
        max_length=MAX_ALBUM_NAME,
        unique=True,
        null=False,
        blank=False,
        verbose_name='Album Name',
    )
    artist = models.CharField(
        max_length=MAX_ARTIST_NAME,
        null=False,
        blank=False,
    )
    genre = models.CharField(
        max_length=MAX_GENRE_NAME,
        choices=MUSICS,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(MIN_PRICE),
        ),
    )

    class Meta:
        ordering = ('pk',)
