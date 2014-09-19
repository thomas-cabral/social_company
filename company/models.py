from django.db import models
from django.contrib.auth.models import Group, User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Company(Group):
    detail = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['name']

        permissions = (
            ('view_company', 'Is member of Company'),
        )

    def __str__(self):
        return '%s' % self.name


@python_2_unicode_compatible
class Event(models.Model):
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ('view_event', 'Is member of Company'),
        )

    def __str__(self):
        return '%s - %s' % (self.title, self.date)