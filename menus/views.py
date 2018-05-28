from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.
from .models import Item

class ItemListView(ListView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemDetailView(DetailView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemCreateView(CreateView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)


class ItemUpdateView(UpdateView):

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)