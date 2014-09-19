from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from .permissions import ViewPermissionOverride, DjangoObjectPermissionsOnly

from company.serializer import CompanySerializer, EventSerializer
from company.models import Company, Event


class CompanyList(generics.ListCreateAPIView):
    permission_classes = (ViewPermissionOverride,)
    serializer_class = CompanySerializer
    model = Company


class CompanyDetailApi(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (ViewPermissionOverride,)
    serializer_class = CompanySerializer
    model = Company


class CompanyEventList(generics.ListCreateAPIView):
    permission_classes = (ViewPermissionOverride,)
    serializer_class = EventSerializer
    model = Event

    def get_queryset(self):
        events = Event.objects.filter(company=self.kwargs['pk'])
        return events