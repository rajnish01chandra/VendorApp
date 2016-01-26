A simple app for vendors/restaurants.  
It allows to:  
  Accept or reject orders  
  Auto reject orders after a timeout of t seconds  
  View active orders : neither accepted nor rejected yet  
  View past orders  
  
Prerequisites:  
Python  2.7  
Django version 1.6.5  
Django-Celery for periodic task  

How to start:  
Edit settings file for app...change database settings
Create tables : $python manage.py syncdb  
Start the server : $python manage.py runserver  
Start celery for scheduling periodic task : $python manage.py celerybeat -S djcelery.schedulers.DatabaseScheduler  

Urls:  

To fill dummy data  
http://localhost:8000/vendor/api/partner/order/fillDB  

To view all past orders:  
http://localhost:8000/vendor/api/partner/order/all  

To view all active orders:  
http://localhost:8000/vendor/api/partner/order/active  


Info:  
Autorejects in 120 seconds.  
