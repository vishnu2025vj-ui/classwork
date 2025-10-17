from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    username = request.GET.get('username', 'Guest')
    form_data = request.GET.items()
    return render(request, 'result.html', {'username': username, 'form_data': form_data})