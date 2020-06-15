from django.shortcuts import render, HttpResponse

# Create your views here.

# def hello(request):
#     return HttpResponse("첫번째 만든 웹페이지에요.")

def hello(request):
    return render(request, 'hello_django/index.html')