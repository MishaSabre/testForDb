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
        fio = request.POST.get('fio')
        specs = request.POST.get('specs')
        payment = request.POST.get('payment')
        percentprofit = request.POST.get('percentporfit')
        diddoctor = -1
        with connection.cursor() as cursor:
            cursor.execute('call "INSERT_DOCTOR"(%s,%s,%s,%s,%s)', (fio, specs, payment, percentprofit, diddoctor))
            cursor.close()
        return redirect('doctors')
    else:
        error = 'Неверная форма'

    form = DoctorForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_doctor.html', data)

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'main/doctor_view.html'
    context_object_name = 'doctor'
def update_doctor(request, pk):
    error = ''
    if request.method == 'POST':
        fio = request.POST.get('fio')
        specs = request.POST.get('specs')
        payment = request.POST.get('payment')
        percentprofit = request.POST.get('percentporfit')
        diddoctor=pk
        with connection.cursor() as cursor:
            cursor.execute('call "UPDATE_DOCTOR"(%s,%s,%s,%s,%s)', (fio, specs, payment, percentprofit, diddoctor))
            cursor.close()
        return redirect('doctors')
    else:
        error = 'Неверная форма'
    form = DoctorForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/add_doctor.html', data)

def doctor_delete(request, pk):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute('call "DELETE_DOCTOR"(%s)', [pk])
            cursor.close()
        return redirect('doctors')

    return render(request, 'main/delete_doctor.html')

def patients(request):
    get_patient = Patient.objects.all()
    return render(request, 'main/patients.html', {'patients' : get_patient})

def add_patient(request):
    error = ''
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronymic = request.POST.get('patronymic')
        bdate = request.POST.get('bdate')
        address = request.POST.get('address')
        didpatient= -1
        with connection.cursor() as cursor:
            cursor.execute('call "INSERT_PATIENT"(%s,%s,%s,%s,%s', (surname, name, patronymic, bdate, address, didpatient))
            cursor.close()
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
def update_patient(request, pk):
    error = ''
    if request.method == 'POST':
        surname = request.POST.get('surname')
        name = request.POST.get('name')
        patronymic = request.POST.get('patronymic')
        bdate = request.POST.get('bdate')
        address = request.POST.get('address')
        with connection.cursor() as cursor:
            cursor.execute('call "UPDATE_PATIENT"(%s,%s,%s,%s,%s, %s)', (surname, name, patronymic, bdate, address, pk))
            cursor.close()
        return redirect('patients')
    else:
        error = 'Неверная форма'

    form = PatientForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_patient.html', data)
def patient_delete(request, pk):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute('call "DELETE_PATIENT"(%s)', [pk])
            cursor.close()
        return redirect('patients')

    return render(request, 'main/delete_patient.html')

def visits(request):
    get_visit = Visits.objects.all()
    return render(request, 'main/visits.html', {'visits' : get_visit})

def add_visit(request):
    error = ''
    if request.method == 'POST':
        iddoctor = request.POST.get('iddoctor')
        idpatient = request.POST.get('idpatient')
        date_of_visit = request.POST.get('date_of_visit')
        idvisits = -1
        with connection.cursor() as cursor:
            cursor.execute('call "INSERT_VISITS"(%s,%s,%s,%s)',
                           (iddoctor, idpatient, date_of_visit, idvisits))
            cursor.close()
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
def update_visit(request, pk):
    error = ''
    if request.method == 'POST':
        iddoctor = request.POST.get('iddoctor')
        idpatient = request.POST.get('idpatient')
        date_of_visit = request.POST.get('date_of_visit')
        idvisits = pk
        with connection.cursor() as cursor:
            cursor.execute('call "UPDATE_VISITS"(%s,%s,%s,%s)',
                           (iddoctor, idpatient, date_of_visit, idvisits))
            cursor.close()
        return redirect('visits')
    else:
        error = 'Неверная форма'

    form = VisitsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_visit.html', data)

def visit_delete(request, pk):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute('call "DELETE_VISITS"(%s)', [pk])
            cursor.close()
        return redirect('visits')

    return render(request, 'main/delete_visit.html')

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
