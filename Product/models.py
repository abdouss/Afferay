
from __future__ import unicode_literals

from django.db import models

# Create your models here.


from django.utils.text import slugify
from django.urls import reverse






class Product(models.Model):


	CATEGORY =  (('','_______________________Voiture _______________________'),
				 ('Citroen','Citroen'),
				 ('Cat cat','Cat cat'),
				 ('Renault 19','Renault 19'),)

	Ville   = (('','_______________________Ville _______________________'),
		       ('Agadir','Agadir'),
		       ('Rabat','Rabat'),
		       ('Casablanca','Casablanca'),
		       ('Tanger','Tanger'),
		      )

	


	Nom_Produit              =models.CharField(max_length=200,blank=True,null=True)

	Description      =models.TextField(blank=True,null=True)

	Category         =models.CharField(max_length=600,choices=CATEGORY)

	Ville            =models.CharField(max_length=600,choices=Ville)

	Created          =models.DateTimeField(auto_now_add=True)

	updated_at       =models.DateTimeField(auto_now=True)


	slug             =models.SlugField(null=True,blank=True)

	Price            =models.CharField(max_length=200,blank=True,null=True)


	Nom_Annonceur    =models.CharField(max_length=200,blank=True,null=True)
	phone_Number     =models.PositiveIntegerField(default=0)









	def __str__(self):

		return self.Nom_Produit


	def get_absolute_url(self):
	    return reverse("product_detail", kwargs={"slug": self.slug})

	class Meta:
	    ordering = ['-Created']

	def _get_unique_slug(self):
	    slug = slugify(self.Nom_Produit)
	    unique_slug = slug
	    num = 1
	    while Product.objects.filter(slug=unique_slug).exists():
	        unique_slug = '{}-{}'.format(slug, num)
	        num += 1
	    return unique_slug

	def save(self, *args, **kwargs):
	    if not self.slug:
	        self.slug = self._get_unique_slug()
	    super(Product, self).save()



class Images(models.Model):
	product   = models.ForeignKey(Product,blank=True,null=True,on_delete=models.CASCADE)
	image    = models.ImageField(upload_to='crop',blank=True)

	def __str__(self):
		return "Addition image"

