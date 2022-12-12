from django.urls import path

from .views import DetailView
urlpatterns=[
    path('Detail/',DetailView.as_view())
]