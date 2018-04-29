from django.db import models

class Index(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	background_image = models.ImageField(blank=True)
	category_img = models.ImageField(blank=True)
	thumbnail_img = models.ImageField(blank=True)

	def __str__(self):
		return self.title


class FolioImage(models.Model):
	index = models.ForeignKey(Index, on_delete=models.PROTECT)
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	image = models.ImageField(blank=True)

	def __str__(self):
		return self.title