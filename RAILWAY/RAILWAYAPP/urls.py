"""RAILWAY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RAILWAYAPP import views
urlpatterns = [
  path("adminhome",views.adminhome),
  path("login",views.loginpage),
  path("railway",views.loginpage),
  path("register",views.TCSave),
  path("tcregisterdisplay",views.registerdisplay),
  path("addtrain",views.AddtrainSave),
  path("addtraindisplay",views.addtraindisplay),
  path("trainroute",views.TrainrouteSave),
  path("trainroutedisplay",views.trainroutedisplay),
  path("passengerlist",views.PassengerSave),
  path("passengerlistdisplay",views.passengerlistdisplay),
  path("tcpassengerlistdisplay",views.tcpassengerlistdisplay),
  path("tchome",views.tchome),

  ]
