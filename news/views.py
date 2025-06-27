from django.shortcuts import render

# Create your views here.

from .models import News

def malumot(request):
    news_list = News.objects.all()
    return render(request, 'loyha.html',{'news_list': news_list})