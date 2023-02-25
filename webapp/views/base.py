from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import GBook


def index_view(request: WSGIRequest):
    records = GBook.objects.exclude(status='blocked')
    context = {'records': records}
    return render(request, 'index.html', context=context)
