from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


index = ListView.as_view(model=Post, template_name='post/index.html')

post_detail = DetailView.as_view(model=Post)