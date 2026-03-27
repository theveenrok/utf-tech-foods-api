# models.py
from django.db import models

from apps.shared.models import TimeStampedModel


class FoodCategory(TimeStampedModel):
    name_ru = models.CharField(
        verbose_name="Russian name",
        help_text="The name of the category in Russian.",
        max_length=255,
        unique=True,
    )
    name_en = models.CharField(
        verbose_name="English name",
        help_text="The name of the category in English.",
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
    name_ch = models.CharField(
        verbose_name="Chinese name",
        help_text="The name of the category in Chinese.",
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )
    order_id = models.SmallIntegerField(default=10, blank=True, null=True)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Menu section"
        verbose_name_plural = "Menu sections"
        ordering = ("name_ru", "order_id")


class Food(TimeStampedModel):
    category = models.ForeignKey(
        "menu.FoodCategory",
        verbose_name="Menu section",
        related_name="foods",
        on_delete=models.CASCADE,
    )

    is_vegan = models.BooleanField(
        verbose_name="Vegan",
        default=False,
    )
    is_special = models.BooleanField(
        verbose_name="Special offer",
        default=False,
    )

    code = models.IntegerField(
        verbose_name="Supplier code",
    )
    internal_code = models.IntegerField(
        verbose_name="App code",
        unique=True,
        null=True,
        blank=True,
    )

    name_ru = models.CharField(
        verbose_name="Russian name",
        max_length=255,
    )
    description_ru = models.CharField(
        verbose_name="Russian description",
        max_length=255,
        blank=True,
        null=True,
    )
    description_en = models.CharField(
        verbose_name="English description",
        max_length=255,
        blank=True,
        null=True,
    )
    description_ch = models.CharField(
        verbose_name="Chinese description",
        max_length=255,
        blank=True,
        null=True,
    )

    cost = models.DecimalField(
        verbose_name="Cost",
        max_digits=10,
        decimal_places=2,
    )

    is_publish = models.BooleanField(
        verbose_name="Published",
        default=True,
    )

    additional = models.ManyToManyField(
        "self",
        verbose_name="Additional products",
        symmetrical=False,
        related_name="additional_from",
        blank=True,
    )

    def __str__(self):
        return self.name_ru
