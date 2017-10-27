from django.shortcuts import render


# Create your views here. Creating now!!
def hello(request):
    return render(request, ' hello.html')
