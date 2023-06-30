from .models import Doctor, Patient, Visits
from django.forms import ModelForm, TextInput, NumberInput, DateInput
from django import forms


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['iddoctor', 'fio', 'specs', 'payment', 'percentprofit']

        widgets = {
            "fio": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО Доктора'
            }),
            "specs": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Спецификация'
            }),
            "payment": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Плата за прием'
            }),
            "percentprofit": NumberInput(attrs={
                'class': 'form-control',
                'min': '0', 'max': '1', 'step': '0.01',
                'placeholder': 'Процент от платы за прием'
            })
        }
class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['idpatient', 'surname', 'name', 'patronymic', 'bdate', 'address']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "bdate": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата рождения YYYY-MM-DD'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адресс'
            })
        }
class VisitsForm(ModelForm):
    class Meta:
        model = Visits
        fields = ['iddoctor', 'idpatient', 'date_of_visit', 'idvisits']

        widgets = {
            "iddoctor": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Доктора'
            }),
            "idpatient": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Пациента'
            }),
            "date_of_visit": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата посещения YYYY-MM-DD'
            }),
            "idvisits": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID Визита'
            })
        }
