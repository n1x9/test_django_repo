from django.db.models import fields
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Hist

class HistListView(ListView):
    model = Hist

class HistDetailView(DetailView):
    model = Hist

class HistCreateView(CreateView):
    model = Hist
    fields = ['name','data','year','image']

class HistUpdateView(UpdateView):
    model = Hist
    fields = ['name','data','year','image']
    template_name_suffix = '_update_form'