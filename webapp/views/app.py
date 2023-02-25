from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from webapp.models import GBook


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


def record_delete_view(request: WSGIRequest, pk):
    record = get_object_or_404(GBook, pk=pk)
    context = {'record': record}
    return render(request, 'delete.html', context=context)


def confirm_delete(request: WSGIRequest, pk):
    record = get_object_or_404(GBook, pk=pk)
    record.delete()
    records = GBook.objects.all()
    context = {'records': records}
    return render(request, 'index.html', context=context)