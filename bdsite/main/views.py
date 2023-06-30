from django.shortcuts import render
def doctors(request):
    return render(request, 'main/doctors.html')

def add_doctor(request):
    return render(request, 'main/add_doctor.html')

def update_doctor(request):
    return render(request, 'main/update_doctor.html')

def delete_doctor(requst):
    return render(requst, 'main/delete_doctor.html')

def patients(request):
    return render(request, 'main/patients.html')

def add_patient(request):
    return render(request, 'main/add_patient.html')

def update_patient(request):
    return render(request, 'main/update_patient.html')

def delete_patient(requst):
    return render(requst, 'main/delete_patient.html')

def visits(request):
    return render(request, 'main/visits.html')

def add_visit(request):
    return render(request, 'main/add_visit.html')

def update_visit(request):
    return render(request, 'main/update_visit.html')

def delete_visit(requst):
    return render(requst, 'main/delete_visit.html')


