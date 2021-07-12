from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.functional import lazy
from django.views.generic import CreateView


from accountapp.models import HelloWorld


def introduce(request):
    if request.method == 'POST':

        temp = request.POST.get('introduce_input')

        new_introduce = HelloWorld()
        new_introduce.text = temp
        new_introduce.save()

        return HttpResponseRedirect(reverse('accountapp:myself'))
    else:
        introduce_list = HelloWorld.objects.all()
        return render(request, 'accountapp/introduce.html',
                      context={'introduce_list': introduce_list})



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url =reverse_lazy('accountapp:introduce')
    template_name ='accountapp/create.html'