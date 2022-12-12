from django.shortcuts import render
from django.http import HttpResponseNotFound
def error_404_view(request,exception):
    return HttpResponseNotFound({"Not Found"})
# Create your views here.
