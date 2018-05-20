# import random
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import RestaurantCreateForm, RestaurantsLocationCreateForm
from .models import RestaurantLocation

# Create your views here.

#function based view

def restaurant_createview(request):
    form = RestaurantsLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        # obj = RestaurantLocation.objects.create(
        #     name = form.cleaned_data.get('name'),
        #     location = form.cleaned_data.get('location'),
        #     category = form.cleaned_data.get('category')
        # )
        return HttpResponseRedirect('/restaurants/')
    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {
        "form" : form,
        "errors" : errors
    }
    return render(request, template_name, context)



def restaurants_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, template_name, context)

def restaurants_detailview(request, slug):
    template_name = 'restaurants/restaurantlocation_detail.html'
    obj = RestaurantLocation.objects.get(slug=slug)
    context = {
        "objects" : obj
    }
    return render(request, template_name, context)

class RestaurantsListView(ListView):

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                    Q(category__iexact=slug) |
                    Q(category__icontains=slug)
                    )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset

class RestaurantsDetailView(DetailView):
    queryset = RestaurantLocation.objects.all() #.filter(category__iexact='I')

    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantsDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id) #pk=rest_id
    #
    #     return obj


class RestaurantCreateView(CreateView):
    form_class = RestaurantsLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'
