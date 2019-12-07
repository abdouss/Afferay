from . import views
from django.urls import path


urlpatterns = [
    path("contacts_view/",views.contacts_view,name="contacts_view"),
   
]
