from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from vendor.models import Order,OrderDetail,FoodItem
from django.core.paginator import Paginator
from django.db.models import Q

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
		return render(request, 'vendors/orders.html', {'orders':pages.page(page).object_list} )

def activeOrders(request):
	if(request.method == 'GET'):
		orders = Order.objects.filter(action = 1)
		return render(request, 'vendors/orders.html', {'orders':orders} )

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
def test_celery(request):
	result = tasks.add(2,3)
	result_one = tasks.sleeptask.delay(10)
	result_two = tasks.sleeptask.delay(10)
	return HttpResponse(result.task_id)