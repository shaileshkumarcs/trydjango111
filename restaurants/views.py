import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#function based view

def home(request):
    num = None
    num = random.randint(0,10000000000)
    some_list = [
        random.randint(0,10000000000),
        random.randint(0,10000000000),
        random.randint(0,10000000000)
    ]
    condition_bool_item = True
    if condition_bool_item:
        num = random.randint(0,1000000000)
    context = {
        "num":num,
        "some_list":some_list
    }
    return render(request,"base.html",context)#response