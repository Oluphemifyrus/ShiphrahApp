from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ShiphrahApp/index.html')

def about(request):
    return render(request, 'ShiphrahApp/about.html')

def contact(request):
    return render(request, 'ShiphrahApp/contact.html')