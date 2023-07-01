from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctors, name="doctors"),
    path('patients', views.patients, name='patients'),
    path('visits', views.visits, name='visits'),
    path('add_doctor', views.add_doctor, name='add_doctor'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('add_visit', views.add_visit, name='add_visit'),
    path('<int:pk>', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('<int:pk>/update', views.update_doctor, name='doctor_update'),
    path('<int:pk>/delete', views.doctor_delete, name='doctor_delete'),
    path('patients/<int:pk>', views.PatientDetailView.as_view(), name='patient_detail'),
    path('patients/<int:pk>/update', views.update_patient, name='patient_update'),
    path('patients/<int:pk>/delete', views.patient_delete, name='patient_delete'),
    path('visits/<int:pk>', views.VisitDetailView.as_view(), name='visit_detail'),
    path('visits/<int:pk>/update', views.update_visit, name='visit_update'),
    path('visits/<int:pk>/delete', views.visit_delete, name='visit_delete'),
    path('payment_rep', views.payment_rep, name='payment_rep'),
    path('receipt_patient', views.receipt_patient, name='receipt_patient')
]