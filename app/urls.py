
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('media',views.media,name="media"),
    path('contact',views.contact,name="contact"),
    path('sendmail',views.sendmail,name="sendmail"),
    path('bus',views.bus,name="bus"),
    path('van',views.van,name="van"),
    path('rickshaw',views.rickshaw,name="rickshaw"),
    path('thankyou',views.thankyou,name="thankyou"),

]
