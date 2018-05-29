# import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from .forms import RestaurantCreateForm, RestaurantsLocationCreateForm
from .models import RestaurantLocation

# Create your views here.

#function based view

# @login_required()
# def restaurant_createview(request):
#     form = RestaurantsLocationCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         if request.user.is_authenticated():
#             instance = form.save(commit=False)
#             # customize
#             # like a pre_save
#             instance.owner = request.user
#             instance.save()
#             return HttpResponseRedirect('/restaurants/')
#         else:
#             return HttpResponseRedirect('/login/')
#     if form.errors:
#         errors = form.errors
#
#     template_name = 'restaurants/form.html'
#     context = {
#         "form" : form,
#         "errors" : errors
#     }
#     return render(request, template_name, context)
#
#
#
# def restaurants_listview(request):
#     template_name = 'restaurants/restaurants_list.html'
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         "object_list" : queryset
#     }
#     return render(request, template_name, context)
#
# def restaurants_detailview(request, slug):
#     template_name = 'restaurants/restaurantlocation_detail.html'
#     obj = RestaurantLocation.objects.get(slug=slug)
#     context = {
#         "objects" : obj
#     }
#     return render(request, template_name, context)

class RestaurantsListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        # print(self.kwargs)
        # slug = self.kwargs.get("slug")
        # if slug:
        #     queryset = RestaurantLocation.objects.filter(
        #             Q(category__iexact=slug) |
        #             Q(category__icontains=slug)
        #             )
        # else:
        #     queryset = RestaurantLocation.objects.all()
        # return queryset
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantsDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user) #.filter(category__iexact='I')

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantsLocationCreateForm
    login_url = '/login'
    template_name = 'form.html'
    #success_url = '/restaurants/'

    def form_valid(self,form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        #instance.save()
        return super(RestaurantCreateView,self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return  context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantsLocationCreateForm
    login_url = '/login'
    template_name = 'restaurants/detail-update.html'
    #success_url = '/restaurants/'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Update Restaurant : {name}'
        return  context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user) #.filter(category__iexact='I')