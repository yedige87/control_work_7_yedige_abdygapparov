from django.urls import path

from webapp.views.app import app_view
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('app', app_view, name='app_view')
]