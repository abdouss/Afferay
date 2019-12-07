from .models import Product,Images
from django import forms
from PIL import Image
from django.forms import ModelForm

class Productform(forms.ModelForm):


    class Meta:

          model = Product
          fields =('Category','Ville','Nom_Produit','Description','Price','Nom_Annonceur','phone_Number')
          labels ={
                  'Nom_Annonceur':'Available Nom de l annonceur ',
                  'phone_Number':'Available phonenumber',
                 
                }
          widgets = {
            'Nom Annonceur': forms.TextInput(attrs={'placeholder': 'Separate item colors with comma e.g red,black,green'}),
            'phoneNumber': forms.TextInput(attrs={'placeholder': 'Separate item size with comma e.g 2,5 or X,ML,M'}),
        }

         

class AdditionImageForm(forms.ModelForm):

    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Images
        fields = ('product',
                  'image',
                  'x',
                  'y',
                  'width',
                  'height')

    def save(self):
        photo = super(AdditionImageForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((400, 400), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo
