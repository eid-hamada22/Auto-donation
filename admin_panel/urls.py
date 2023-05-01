from django.urls import path
from . import views

app_name = 'admin_panel'
urlpatterns = [
    path('', views.index, name="index"),
    path('beneficiary', views.beneficiary, name="beneficiary"),
    path('donation', views.donation, name="donation"),
    path('delivery_point', views.delivery_point, name="delivery_point"),
    path('delivery_point_admin', views.delivery_point_admin, name="delivery_point_admin"),
    path('item', views.item, name="item"),
    path('item_desire', views.item_desire, name="item_desire"),
    path('item_demand', views.item_demand, name="item_demand"),
    path('monthly_graphic_report', views.monthly_graphic_report, name="monthly_graphic_report"),
    path('message', views.message, name="message"),

]
