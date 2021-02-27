from django.db import models


class ProductCategory(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Product(models.Model):	
	product_id = models.AutoField(primary_key=True)
	cat_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.FloatField()
	img1 = models.ImageField(upload_to="shop/products")
	in_stock = models.BooleanField(default=True)

	def __str__(self):
		return self.name

class ContactResponse(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=50)
	phone = models.CharField(max_length=100)
	message = models.TextField()

	def __str__(self):
		return self.name

		