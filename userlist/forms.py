from django import forms
from django.core.exceptions import ValidationError

class AddPatientForm(forms.Form):

	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	age = forms.IntegerField(required=True)
	address = forms.CharField(required=True,
        widget=forms.Textarea)
	contact_number = forms.CharField(required=True)
	#contact_email = forms.EmailField(required=True)

 #   STATUS = (
 #       ('v', 'Verified'),
  #      ('u', 'Unverified'),
        
   # )
  #  verify_status = forms.ChoiceField(choices = STATUS, label="Verification Status", initial='u', widget=forms.Select())

