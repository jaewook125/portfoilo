from django.shortcuts import render
from .models import Index, FolioImage
from django.views.generic import ListView, DetailView


index = ListView.as_view(model=Index, template_name='blog/index.html')

folio_detail = DetailView.as_view(model=FolioImage)