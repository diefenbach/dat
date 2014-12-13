from django.shortcuts import render_to_response
from django.template import RequestContext


def display_view(request, template_name):
    return render_to_response(template_name, RequestContext({

    }))
