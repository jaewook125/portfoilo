from django.contrib import admin
from .models import Index, FolioImage

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
	list_display = ['title','background_image']


@admin.register(FolioImage)
class IndexAdmin(admin.ModelAdmin):
	list_display = ['title','image']