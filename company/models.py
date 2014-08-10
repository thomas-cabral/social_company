from django.db import models
from django.contrib.auth.models import Group, User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Company(models.Model):
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['name']

        permissions = (
            ('view_company', 'Is member of Company'),
        )

    def __str__(self):
        return '%s' % self.name