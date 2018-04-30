from django.contrib import admin
from .models import Index, FolioImage
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
	list_display = ['title','category_img']


@admin.register(FolioImage)
class IndexAdmin(SummernoteModelAdmin):
	list_display = ['title','image']
	list_fields = ['title','image']
	summernote_fields = ['content']