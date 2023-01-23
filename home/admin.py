from django.contrib import admin
from .models import department, architect, booking
# Register your models here.
admin.site.register(department)
admin.site.register(architect)

class bookingadmin(admin.ModelAdmin):
    list_display = ('id','client_name', 'client_phone', 'client_email', 'arc_name', 'appnt_date','booked_on')

admin.site.register(booking,bookingadmin)