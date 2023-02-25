from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def record_add_view(request: WSGIRequest):
    context = {
        'key': 'value'
    }
    return render(request, 'index.html', context=context)

def record_edit_view(request: WSGIRequest):
    context = {
        'key': 'value'
    }
    return render(request, 'index.html', context=context)

def record_delete_view(request: WSGIRequest):
    context = {
        'key': 'value'
    }
    return render(request, 'index.html', context=context)