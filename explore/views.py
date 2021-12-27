from django.shortcuts import render


def explore(request):
    return render(request, 'explore.html')