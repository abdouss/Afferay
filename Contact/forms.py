from django import forms
from django.forms import ModelForm
from . models import Contact
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.fields import RichTextField

class contact_email_form(ModelForm):
	class Meta:
		model = Contact
		fields = ['Name','Message']
