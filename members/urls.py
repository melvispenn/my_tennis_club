from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path("i18n/", include("django.conf.urls.i18n")),
    path('memberdetails/<int:id>/', views.details, name='details')
]
