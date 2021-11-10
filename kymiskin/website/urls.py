from django.urls import path
from .import views


app_name='website'

urlpatterns = [
	path('', views.index, name='index'),
	path('services', views.services, name='services'),
	path('about', views.about, name="about"),
	path('contact', views.contact, name="contact"),
	path('service-detail/<int:pk>/', views.service_details, name='detail'),

	path('skin-care-treatment/details', views.skin_details, name='skin_details'),
	path('body-treatment/details', views.body_details, name='body_details'),
	path('weight-management/details', views.weight_details, name='weight_details'),
]