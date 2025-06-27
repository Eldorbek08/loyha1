
from django.shortcuts import render

# Create your views here.

from .models import Group

def malumot(request):
    group_list = Group.objects.all()
    return render(request, 'loyha.html',{'group_list': group_list})