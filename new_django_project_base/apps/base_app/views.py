from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings

def base_view(request):
    context_dict = {}
    if settings.RUNNING_ENVIRONMENT=='development':
        context_dict['DEVELOPMENT']=True
    return render(request, 'index.html', context_dict)

