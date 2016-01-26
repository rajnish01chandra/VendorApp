from django.db import models

class Vendor(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Order(models.Model):
	actionChoice = (
		(1, 'Active'),
		(2, 'Accept'),
		(3, 'Reject')
		)
	vendor = models.ForeignKey(Vendor)
	orderTime = models.IntegerField()
	action = models.IntegerField(choices = actionChoice, default = 1)

class FoodItem(models.Model):
	name = models.CharField(max_length=30)
	price = models.DecimalField(decimal_places=2, max_digits=5)
	category = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class OrderDetail(models.Model):
	order = models.ForeignKey(Order)
	foodItem = models.ForeignKey(FoodItem)
	quantity = models.IntegerField()
