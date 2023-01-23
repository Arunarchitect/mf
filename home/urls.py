from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('architects',views.architects, name='architects'),
    path('booking',views.bookings, name='bookings'),
    path('contact',views.contact, name='contact'),
    path('department',views.departments, name='department'),
]