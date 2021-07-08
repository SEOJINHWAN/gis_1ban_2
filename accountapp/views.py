from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def introduce(request):
    if request.method == 'POST':
        return  render(request, 'accountapp/introduce.html',
                       context={'text' : 'POST METHOD'})
    else:
        return render(request, 'accountapp/introduce.html',
                      context={'text': 'Enjoy_Your_Life'})
