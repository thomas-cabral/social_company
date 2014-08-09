from django.db import models
from django.contrib.auth.models import Group, User
from django.utils.encoding import python_2_unicode_compatible


class CompanyManager(models.Manager):
    """
    Lets us do querysets limited to families that have
    currently enrolled students, e.g.:
        Family.has_students.all()
    """
    def get_query_set(self):
        return super(CompanyManager, self).get_query_set().filter(student__enrolled=True).distinct()


@python_2_unicode_compatible
class Company(Group):
    notes = models.TextField(blank=True)

    # Two managers for this model - the first is default
    # (so all families appear in the admin).
    # The second is only invoked when we call
    # Family.has_students.all()
    objects = models.Manager()
    has_users = CompanyManager()

    class Meta:
        verbose_name_plural = "Companies"
        ordering = ['name']

        permissions = (
            ('view_company', 'Is member of Company'),
        )

    def __str__(self):
        return '%s' % self.name