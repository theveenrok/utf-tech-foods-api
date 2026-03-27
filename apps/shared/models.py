from django.db.models import DateTimeField, Model


class TimeStampedModel(Model):
    created_at = DateTimeField(
        verbose_name="Created At",
        help_text="The date and time this record was created.",
        auto_now_add=True,
    )
    updated_at = DateTimeField(
        verbose_name="Updated At",
        help_text="The date and time this record was last updated.",
        auto_now=True,
    )

    class Meta:
        abstract = True
