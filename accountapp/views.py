from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def introduce(request):
    return render(request, 'accountapp/introduce.html')

