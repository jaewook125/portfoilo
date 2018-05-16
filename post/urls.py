from django.urls import path, include
from . import views

app_name = 'post'

urlpatterns =[
	path('', views.index, name='index'),
	path('<int:pk>', views.post_detail, name='post_detail'),
]