from django.contrib import admin
from .models import Doctor, Patient, Visits

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Visits)