from django.shortcuts import render, get_object_or_404
from django.views import generic

from guardian.core import ObjectPermissionChecker

# Create your views here.


from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Company
from guardian.shortcuts import get_objects_for_user


def user_dashboard(request, template_name='company/index.html'):
    company = get_objects_for_user(request.user, 'company.view_company')

    return render_to_response(template_name, {'companies': company},
                              context_instance=RequestContext(request))


def company_detail(request, pk):
    company = Company.objects.get(id=pk)
    company_object = get_object_or_404(Company, pk=pk)
    template = 'company/public_detail.html'
    # check if user has permission to view, if so render private template
    if request.user.is_authenticated():
        user = request.user
        checker = ObjectPermissionChecker(user)
        if checker.has_perm('view_company', company):
            template = 'company/secure_detail.html'

    return render_to_response(template, {'company': company_object})


class CreateCompany(generic.CreateView):
    model = Company
