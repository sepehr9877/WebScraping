from django.urls import path

from .views import DetailView
urlpatterns=[
    path('',DetailView.as_view())
]