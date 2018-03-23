import time
import datetime

from django.shortcuts import render
from django.http import HttpResponse

from .models import Flow

import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

def index(request):
    latest = Flow.objects.latest('timestamp')
    return HttpResponse("Latest 'Flow': " + str(latest.val) + ' ' + str(latest.timestamp))

def minute(request):
    past_minute = map(lambda x: (x.val, x.timestamp), Flow.objects.filter(timestamp__gt=int(time.time())-60))
    return HttpResponse("This is where we show the flow for the last minute" + str(list(past_minute)))

def hour(request):
    past_hour = Flow.objects.filter(timestamp__gt=int(time.time())-36000)
    return HttpResponse("This is where we show the flow for the last hour" + str(len(past_hour)))

def day(request):
    return HttpResponse("This is where we show the flow for the last day")

def week(request):
    return HttpResponse("This is where we show the flow for the last week")

def test(request):
    fig = Figure()
    ax = fig.add_subplot(111)
    x=[]
    y=[]
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now += delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x,y,'-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

