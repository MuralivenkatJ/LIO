from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login2.html')

def register(request):
    return render(request, 'signup2.html')