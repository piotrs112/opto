from django.contrib import admin

from dash.models import *
# Register your models here.

admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Parameters)
admin.site.register(Appointment)