from django.urls import path

from webapp.views.app import record_add_view, record_edit_view, record_delete_view, confirm_delete
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add', record_add_view, name='record_add'),
    path('edit/<int:pk>', record_edit_view, name='record_edit'),
    path('delete/<int:pk>', record_delete_view, name='record_delete'),
    path('delete_yes/<int:pk>', confirm_delete, name='confirm_delete'),
]