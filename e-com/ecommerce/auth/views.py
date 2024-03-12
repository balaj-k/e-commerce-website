from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Auth

def personal(request):
    member = Auth.objects.all().values()
    template = loader.get_template('All_data.html')
    context = {
        'member' : member,
    }
    return HttpResponse(template.render(context, request))
