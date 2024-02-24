from email.policy import default
from enum import auto, unique
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid


class Profile(models.Model):
    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(12),
        ],
        blank=False,
        null=False,
    )
    password = models.CharField(
        max_length=30,
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    profile_picture = models.URLField(
        blank=False,
        null=False,
    )

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return ''


class Blog(models.Model):
    title = models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True,
    )
    category = models.CharField(
        max_length=30,
        choices=[
            ("Месо", "Месо"),
            ("Риба", "Риба"),
            ("Млечни продукти", "Млечни продукти"),
            ("Зърнени храни", "Зърнени храни"),
            ("Плодове и зеленчуци", "Плодове и зеленчуци"),
            ("Добавки/Сосове", "Добавки/Сосове"),
            ("Други", "Други"),
        ],
        blank=False,
        null=False,
    )
    utility = models.FloatField(
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        ]
    )
    difficulty_level = models.IntegerField(
        validators=[
            MinValueValidator(1),
        ],
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        blank=False,
        null=False,
    )
    summary = models.TextField(
        blank=True,
        null=True,
    )
    profile = models.ForeignKey(
        Profile,
        related_name='blog',
        on_delete=models.CASCADE,
        default=Profile.objects.first,
    )
