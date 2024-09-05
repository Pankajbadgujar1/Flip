from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Shophome"),
    path("about/", views.about, name="aboutus"),
    path("contact/", views.contact, name="contactus"),
    path("search/", views.search, name="search"),
    path("productView/", views.productView, name="productView"),
    path("checkout/", views.checkout, name="checkout"),    
]