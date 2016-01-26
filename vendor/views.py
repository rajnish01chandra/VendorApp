from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from vendor.models import Order,OrderDetail,FoodItem,Vendor
from django.core.paginator import Paginator
from django.db.models import Q
import time
import calendar

# Create your views here.
def action(request):
	if(request.method == 'POST'):
		val = request.POST.get('orderId')
		orderId = 0
		try:
			orderId = int(val)
		except:
			return HttpResponseBadRequest("Invalid Order")
		order = Order.objects.get(id = orderId)
		if( 'accept' in request.POST ):
			order.action = 2
		elif( 'reject' in request.POST ):
			order.action = 3
		order.save()
		return HttpResponseRedirect("all")

def getOrders(request):
	if(request.method == 'GET'):
		val = request.GET.get('page', '1')
		page = 1
		try:
			page = int(val)
		except:
			page = 1

		orders = Order.objects.filter(~Q(action = 1))
		pages = Paginator(orders,10)
		if(page > pages.num_pages):
			page = pages.num_pages
		elif(page<1):
			page = 1
		return render(request, 'vendors/orders.html', {'orders':pages.page(page).object_list, 'page':'all'} )

def activeOrders(request):
	if(request.method == 'GET'):
		orders = Order.objects.filter(action = 1)
		return render(request, 'vendors/orders.html', {'orders':orders, 'page':'active'} )

def orderDetail(request):
	if(request.method == 'GET'):
		val = request.GET.get('orderId','0')
		orderId = 0
		try:
			orderId = int(val)
		except:
			orderId = 0
		total=0
		if( not orderId == 0):
			order = Order.objects.get(id=orderId)
			orderItems = OrderDetail.objects.filter(order = order)
			for i in orderItems:
   				total=total+i.foodItem.price*i.quantity
			
			return render(request, 'vendors/orderDetails.html', {'order':order, 'orderItems': orderItems,'total':total})

def fillDB(request):
	vendor = Vendor(
			name = "Delhi Darbar",
			address = "Marathahalli"
		)
	vendor.save()

	foodItem1 = FoodItem(
			name = "Paneer Palak Masala",
			price = 110,
			category = "Main Course\Veg"
		)
	foodItem1.save()
	foodItem2 = FoodItem(
			name = "Chicken Chilli",
			price = 105,
			category = "Starter\Non Veg"
		)
	foodItem2.save()

	order1 = Order(
			vendor = vendor,
			orderTime = calendar.timegm(time.gmtime()),
			action = 1
		)
	order1.save()
	order2 = Order(
			vendor = vendor,
			orderTime = calendar.timegm(time.gmtime())+120,
			action = 1
		)
	order2.save()
	order3 = Order(
			vendor = vendor,
			orderTime = calendar.timegm(time.gmtime())+360,
			action = 1
		)
	order3.save()

	orderDetail1 = OrderDetail(
			order = order1,
			foodItem = foodItem1,
			quantity = 2
		)
	orderDetail1.save()
	orderDetail2 = OrderDetail(
			order = order1,
			foodItem = foodItem2,
			quantity = 1
		)
	orderDetail2.save()

	orderDetail3 = OrderDetail(
			order = order2,
			foodItem = foodItem1,
			quantity = 1
		)
	orderDetail3.save()

	orderDetail4 = OrderDetail(
			order = order3,
			foodItem = foodItem2,
			quantity = 2
		)
	orderDetail4.save()
	return render(request, 'vendors/index.html')