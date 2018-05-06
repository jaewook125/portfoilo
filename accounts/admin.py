from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class IndexAdmin(admin.ModelAdmin):
	list_display = ['user','nickname','region']