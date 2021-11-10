from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.http import HttpResponse
import csv
from django.core.mail import send_mail


def addcomment(request, pk):
    url = request.META.get('HTTP_REFERER')
    #return HttpResponse(url)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.item_id = pk 
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.info(request, "Your Review has been sent. Thanks for your feedback.")
            return HttpResponseRedirect(url)
        else:
            messages.info(request, "Failed. Your form was not valid")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

def index(request):
	return render(request, 'index.html')	

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        message = message + ". Sender Address: "+email
        recipient_list = [settings.EMAIL_HOST_USER]
        subject = 'Kymiskin Website - Contact Form'
        email_from = email        
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        return render(request, "contact.html")
    else:
        return render(request, "contact.html")

def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "service.html")

def service_details(request, pk):
	return render(request, "service-detail.html")

#Services Details Pages

def skin_details(request):
    return render(request, "skin-detail.html")

def body_details(request):
    return render(request, "body-detail.html")

def weight_details(request):
    return render(request, "weight-detail.html")


