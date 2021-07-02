from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def ai(request):
    return render(request, 'ai.html')


def software(request):
    return render(request, 'software.html')


def cloud(request):
    return render(request, 'cloud.html')


def cont(request):
    return render(request, 'contact.html')

