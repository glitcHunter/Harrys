from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    '''odpowiedź na żądanie'''
    return HttpResponse('<html><title>lista</title></html>')
