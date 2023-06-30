from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctors, name="doctors"),
    path('patients', views.patients, name='patients'),
    path('visits', views.visits, name='visits'),
    path('add_doctor', views.add_doctor, name='add_doctor'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('add_visit', views.add_visit, name='add_visit'),
    path('delete_doctor', views.delete_doctor, name='delete_doctor'),
    path('delete_patient', views.delete_patient, name='delete_patient'),
    path('delete_visit', views.delete_visit, name='delete_visit'),
    path('update_doctor', views.update_doctor, name='update_doctor'),
    path('update_patient', views.update_patient, name='update_patient'),
    path('update_visit', views.update_visit, name='update_visit')
]