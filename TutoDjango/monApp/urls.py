from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home_default"), # sans paramètre
    path("home/<str:param>/", views.home, name="home_with_param"), # avec paramètre
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
]
