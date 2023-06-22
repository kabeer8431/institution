from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable': 'This is verified'
    }
    return render(request, 'index.html', context)