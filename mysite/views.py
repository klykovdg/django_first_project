from django.http import HttpResponse, Http404, HttpRequest
from django.shortcuts import render
import datetime


def hello(request):
    return HttpResponse('Hello my World!')


def get_date(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


def hours_ahead(request, hour):
    try:
        hour = int(hour)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=hour)
    return render(request, 'hours_ahead.html', {'hour': hour, 'next_time': dt})


def display_meta(request: HttpRequest):
    val = request.META.items()
    return render(request, 'meta.html', {'meta_val': val})