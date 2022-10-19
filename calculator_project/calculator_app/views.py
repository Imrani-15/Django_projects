from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'calculator_app/index.html')


def submit(request):
    q = request.GET['query']
    try:
        ans = eval(q)
        mydictionary = {
            "q": q,
            "ans": ans,
            "error": False,
            "result": True
        }
        return render(request, 'calculator_app/index.html', context=mydictionary)
    except:
        mydictionary = {
            "error": True,
            "result": False

        }
        return render(request, 'index.html', context=mydictionary)



