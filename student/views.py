from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login1.html')

def register(request):
    return render(request, 'signup1.html')