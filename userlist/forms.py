from django import forms
from django.core.exceptions import ValidationError
from .models import Patient

class AddPatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields =('first_name', 'last_name' ,'age','address','contact_no',)


class StatusChangeForm(forms.Form):
    STATUS = (
        ('v', 'Verified'),
        ('u', 'Unverified'),
    )

    verify_status = forms.ChoiceField(choices = STATUS, label="Verification Status", initial='u', widget=forms.Select())

