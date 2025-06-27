from django.shortcuts import render

# Create your views here.

from .models import Loyha

def malumot(request):
    loyha_list = Loyha.objects.all()
    return render(request, 'loyha.html',{'loyha_list': loyha_list})