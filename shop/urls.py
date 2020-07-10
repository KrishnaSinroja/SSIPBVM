from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="Checkout"),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('viewprofile/', views.viewprofile, name='viewprofile'),


]
app_name='shop'
