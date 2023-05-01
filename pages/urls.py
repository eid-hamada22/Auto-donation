from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'pages'
urlpatterns = [
    path('', views.index, name="index"),
    path('add_donations', views.add_donations, name="add_donations"),
    path('login', views.login, name="login"),

]
