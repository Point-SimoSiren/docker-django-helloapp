from django.shortcuts import render
# from django.http import HttpResponse

'''def hello(request):
    return HttpResponse("Hello from Django & Docker!")
    '''

def hello(request):
    return render (request, "index.html")
