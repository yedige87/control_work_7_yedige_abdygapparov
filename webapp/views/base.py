from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_view(request: WSGIRequest):
    context = {
        'key': 'value'
    }
    return render(request, 'index.html', context=context)
