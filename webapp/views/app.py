from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404

from webapp.forms import RecordForm
from webapp.models import GBook


def record_add_view(request: WSGIRequest):
    if request.method == 'GET':
        form = RecordForm()
        return render(request, 'add.html', context={'form': form})
    form = RecordForm(data=request.POST)
    print(form.__dict__)
    if not form.is_valid():
        return render(request, 'add.html', context={'form': form})
    else:
        record_data = {
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'text': request.POST.get('text'),
                }
        GBook.objects.create(**record_data)
        records = GBook.objects.all()
        context = {'records': records}
        return render(request, 'index.html', context=context)


def record_edit_view(request: WSGIRequest, pk):
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
