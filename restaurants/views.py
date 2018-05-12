import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

#function based view

def home(request):
    num = None
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
    return render(request,"home.html",context)#response

def about(request):

    context = {

    }
    return render(request,"about.html",context)#response

def contact(request):
    context = {

    }
    return render(request, "contact.html", context)  # response

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context =super(HomeView,self).get_context_data(*args, **kwargs)
        #print(context)
        num = None
        some_list = [
            random.randint(0, 10000000000),
            random.randint(0, 10000000000),
            random.randint(0, 10000000000)
        ]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 1000000000)
        context = {
            "num": num,
            "some_list": some_list
        }
        return context

