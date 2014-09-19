from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from .models import Company, Event
# Register your models here.


class CompanyAdmin(GuardedModelAdmin):
    pass
admin.site.register(Company, CompanyAdmin)


class EventAdmin(GuardedModelAdmin):
    pass
admin.site.register(Event, EventAdmin)