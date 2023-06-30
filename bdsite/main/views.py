import psycopg2
from django.shortcuts import render, redirect
from .models import Doctor, Patient, Visits
from .forms import DoctorForm, PatientForm, VisitsForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.db import connection


def doctors(request):
    get_doctor = Doctor.objects.all()
    return render(request, 'main/doctors.html', {'doctors' : get_doctor})

def add_doctor(request):
    error = ''
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
        else:
            error = 'Неверная форма'


    form = DoctorForm()
    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'main/add_doctor.html', data)

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'main/doctor_view.html'
    context_object_name = 'doctor'
class DoctorUpdateView(UpdateView):
    model = Doctor
    template_name = 'main/add_doctor.html'

    form_class = DoctorForm

class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = '/'
    template_name = 'main/delete_doctor.html'

def patients(request):
    get_patient = Patient.objects.all()
    return render(request, 'main/patients.html', {'patients' : get_patient})

def add_patient(request):
    error = ''
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients')
        else:
            error = 'Неверная форма'

    form = PatientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_patient.html', data)
class PatientDetailView(DetailView):
    model = Patient
    template_name = 'main/patient_view.html'
    context_object_name = 'patient'
class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'main/add_patient.html'

    form_class = PatientForm

class PatientDeleteView(DeleteView):
    model = Doctor
    success_url = '/patients'
    template_name = 'main/delete_patient.html'

def visits(request):
    get_visit = Visits.objects.all()
    return render(request, 'main/visits.html', {'visits' : get_visit})

def add_visit(request):
    error = ''
    if request.method == 'POST':
        form = VisitsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visits')
        else:
            error = 'Неверная форма'

    form = VisitsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_visit.html', data)
class VisitDetailView(DetailView):
    model = Visits
    template_name = 'main/visits_view.html'
    context_object_name = 'visit'
class VisitUpdateView(UpdateView):
    model = Visits
    template_name = 'main/add_visit.html'

    form_class = VisitsForm

class VisitDeleteView(DeleteView):
    model = Visits
    success_url = '/visits'
    template_name = 'main/delete_visit.html'

def payment_rep(request):

    first_date = request.POST.get('first')
    second_date = request.POST.get('second')
    with connection.cursor() as cursor:
        cursor.execute('SELECT * from "SALARY_OF_DOCTORS"(%s,%s)', (first_date, second_date))
        rows = cursor.fetchall()
        cursor.close()
    context = {'rows': rows}
    return render(request, 'main/payment_rep.html', context)

def receipt_patient(request):

    first_date = request.POST.get('first')
    second_date = request.POST.get('second')
    pid = request.POST.get('third')
    with connection.cursor() as cursor:
        cursor.execute('SELECT * from "RECEIPT_OF_PATIENT"(%s,%s,%s)', (first_date, second_date, pid))
        rows = cursor.fetchall()
        cursor.close()
    context = {'rows': rows}
    return render(request, 'main/receipt_patient.html', context)
