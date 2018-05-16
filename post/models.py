from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	title = models.CharField(max_length=20)
	content = models.TextField()

	def __str__(self):
		return self.title
		
class SummerNote(summer_model.Attachment):
    summer_field = summer_fields.SummernoteTextField(default='')

