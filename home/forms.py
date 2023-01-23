from django import forms

from. models import booking

class DateInput(forms.DateInput):
    input_type= 'date'

class bookingform(forms.ModelForm):
    class Meta: 
        model= booking
        fields = '__all__'


        widgets = {
            'appnt_date': DateInput(),
         }

        labels= {
            'client_name' : 'Your Name',
            'client_phone' : 'Phone Number',
            'client_email' : 'E-mail',
            'arc_name' : 'Architect',
            'appnt_date' : 'Appointment Date',
        }
