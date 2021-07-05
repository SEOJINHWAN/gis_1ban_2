from django.urls import path

from accountapp.views import introduce

app_name = 'accountapp'

urlpatterns = [
    path('introduce/', introduce, name='myself')
]