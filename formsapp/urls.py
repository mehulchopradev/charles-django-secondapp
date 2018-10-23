from django.urls import path
from formsapp import views

urlpatterns = [
    path('contact-us/', views.contactus),
    path('register/', views.register)
]
