from django.conf.urls import patterns, url
from django.views.generic import ListView
from vendor.models import Vendor
from django.conf import settings

urlpatterns = patterns('vendor.views',
    url(r'^$',
        ListView.as_view(
            model=Vendor,
            template_name='vendors/index.html'),
        name='index'),
    url(r'^api/partner/order/action', 'action',name='action'),
    url(r'^api/partner/order/all', 'getOrders', name='getOrders'),
    url(r'^api/partner/order/active', 'activeOrders',name='activeOrders'),
    url(r'^api/partner/order/orderDetail', 'orderDetail',name='orderDetail'),
    url(r'^api/partner/order/fillDB', 'fillDB',name='fillDB')
)