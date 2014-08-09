from django.shortcuts import render

# Create your views here.


from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Company
from guardian.shortcuts import get_objects_for_user


def user_dashboard(request, template_name='company/index.html'):
    company = get_objects_for_user(request.user, 'company.view_company')
    return render_to_response(template_name, {'company': company},
        RequestContext(request))