from django.shortcuts import render
from django.http import HttpResponse

from .models import Flow

def index(request):
    latest = Flow.objects.latest('timestamp')
    return HttpResponse("Latest 'Flow': " + str(latest.val))
