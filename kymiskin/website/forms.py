from django import forms
from .models import Appointments

#Customers
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointments
        fields = ['name', 'phone', 'email','service','country', 'region', 'town', 'date']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not phone:
            raise forms.ValidationError('This field is required')
        return phone
    
    def clean_country(self):
        country = self.cleaned_data.get('country')
        if not country:
            raise forms.ValidationError('This field is required')
        return country

    def clean_region(self):
        region = self.cleaned_data.get('region')
        if not region:
            raise forms.ValidationError('This field is required')
        return region

    def clean_town(self):
        town = self.cleaned_data.get('town')
        if not town:
            raise forms.ValidationError('This field is required')
        return town

    def clean_service(self):
        service = self.cleaned_data.get('service')
        if not service:
            raise forms.ValidationError('This field is required')
        return service

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date:
            raise forms.ValidationError('This field is required')
        return date

  