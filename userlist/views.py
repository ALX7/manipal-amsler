from django.shortcuts import render
from userlist.forms import AddPatientForm
from django.http import HttpResponseRedirect

# Create your views here.
from .models import Patient, Doctor, AmslerGrid, Hospital

def index(request):
    """
    View function for home page of site.
    """
    num_patients=Patient.objects.all().count()
    num_doctors=Doctor.objects.all().count()
    # Available books (status = 'a')
    #num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'front.html',
        context={'num_patients':num_patients,'num_doctors':num_doctors},
    )

from django.views import generic

class PatientListView(generic.ListView):
    model = Patient
    def get_queryset(self):
        return Patient.objects.filter(doctor = self.request.user)
class PatientDetailView(generic.DetailView):
    model = Patient
    paginate_by = 10

def about(request):
	return render(
		request,
		'about.html',
		)
from django.shortcuts import get_object_or_404	
def amsler(request, pk, uid):
	res = get_object_or_404(AmslerGrid, uid=uid)
	return render(
		request,
		'amsler.html',
		{'amsler_score':res.amsler_score, 'first_name':res.patient.first_name, 'last_name':res.patient.last_name, 'status': res.get_status_display} 
		)
   # return render( request, 'amsler.html', {'amsler_score':amsler_score} 
   # )
def addpatient(request):
    form_class = AddPatientForm
    
    return render(request, 'addpatient.html', {
        'form': form_class,
    })   