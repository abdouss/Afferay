from . import views
from django.urls import path

urlpatterns = [
	
	    path('',views.HomePage.as_view(),name="Homepage"),
	    path('Create/',views.product_form,name='Createproduct'),
	    path(r'Listing/',views.product_list, name='product_list'),

	   	path(r'Listingcrops/',views.photo_list, name='product_list'),

	    path(r'product_detailing/<slug>/',views.product_detail, name='product_detail'),
	    path(r'Filter/', views.Filter, name='Filter'),
	   	path(r'product_update/<slug>/',views.product_update, name='product_update'),
	   	path(r'product_delete/<slug>/',views.product_delete, name='product_delete'),
	   	path('Searchproduit/',views.Search,name='Searchproduit'),



]
