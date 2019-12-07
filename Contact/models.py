
# Create your models here.
from django.db import models

class Contact(models.Model):
	Name = models.CharField(max_length=500)
	Message = models.TextField()
	created_at  = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
