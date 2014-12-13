from django.shortcuts import render_to_response
from django.template import RequestContext


def {{ app_name }}_view(request, template_name="{{ app_name }}.html"):
    return render_to_response(template_name, RequestContext(request, {

    }))
