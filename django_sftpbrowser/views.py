from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def browse_page(request, input_path=None):
    return HttpResponse(f'<html>Welcome to <span>{input_path}</span></html>')
