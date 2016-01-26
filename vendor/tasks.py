from djcelery import celery
from vendor.models import Order
import time
import calendar

@celery.task
def add(x,y):
	return x + y

@celery.task
def updateOrder(t):
	print str(t), 'task'
	orders = Order.objects.all()
	for order in orders:
		o_time=order.orderTime
		c_time=calendar.timegm(time.gmtime())
		if(c_time - o_time > t):
			order.action=3
			order.save()
	return t