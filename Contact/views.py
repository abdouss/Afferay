from django.shortcuts import render

# Create your views here.
from .forms import contact_email_form

def contacts_view(request):
	context = {}
	form = contact_email_form()
	context['form']=form
	return render(request,"Contacts/contact.html",context)