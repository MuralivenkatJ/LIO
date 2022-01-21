from django.shortcuts import render, redirect

from .forms import instituteForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = instituteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('explore')
        return render(request, 'signup3.html')
    else:
        return render(request, 'signup3.html')