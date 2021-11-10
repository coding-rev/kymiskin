from django.contrib import admin
from .models import Appointments


class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'service', 'date', 'paid']
    list_filter = ['paid']
    

admin.site.site_header = 'Kymiskin & Laser Med-Spa - Admin'
admin.site.site_title = 'Kymiskin & Laser Med-Spa - Admin'

#How to unregister Default fields( Eg: Group)
from django.contrib.auth.models import Group, User
admin.site.unregister(Group)
admin.site.unregister(User)


# Register your models here.
admin.site.register(Appointments, AppointmentsAdmin)


