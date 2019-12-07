from django.shortcuts import render

# Create your views here.
from django.views.generic import (View,TemplateView,
	                              ListView,DetailView,
	                              CreateView,DeleteView,UpdateView)

from django.http import HttpResponse
from .forms import Productform,AdditionImageForm
from Product.models import Product,Images
from django.forms.models import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from .filters import UserFilter
from django.core.paginator import Paginator



class HomePage(TemplateView):

	template_name ="Product/home.html"



def product_form(request):

	photos = Images.objects.all()

	imageformset =modelformset_factory(Images,fields=('image',),extra=2)
	if request.method =='POST':
			form    =Productform(request.POST, request.FILES)
			formset =imageformset(request.POST or None,request.FILES or None)
			if form.is_valid() and formset.is_valid():
				product = form.save(commit=False)
				product.user = request.user
				product.save() 

				for f in formset:

					try:
						photo =Images(product=product,image =f.cleaned_data['image'])
						photo.save()
					except Exception as e:
						break
				return redirect(product.get_absolute_url())

	else:
			form =Productform()
			formset =imageformset(queryset=Images.objects.none())


	context ={"form":form,"formset":formset,'photos': photos}
	context['header'] ="Upload your products"

	return render(request, "Product/form.html",context)






def product_list(request):
    categories = Product.objects.all()
    paginator = Paginator(categories, 2)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = { "categories": categories,"contacts":contacts }
    return render(request, "Product/product_list.html", context)


def product_detail(request, slug=None):
    proddetail = get_object_or_404(Product, slug=slug)
    context = { "proddetail": proddetail,}
    return render(request, "Product/product_detail.html", context)


def Filter(request):
    product_list = Product.objects.all()
    user_filter = UserFilter(request.GET, queryset=product_list)
    return render(request, 'Product/p_list.html', {'filter': user_filter})

def product_update(request, slug=None):

	photos = Images.objects.all()
	instance = get_object_or_404(Product, slug=slug)
	imageformset =modelformset_factory(Images,fields=('image',),extra=2)
	if request.method =='POST':
			form    =Productform(request.POST, request.FILES)
			formset =imageformset(request.POST or None,request.FILES or None)
			if form.is_valid() and formset.is_valid():
				product = form.save(commit=False)
				product.user = request.user
				product.save() 

				for f in formset:

					try:
						photo =Images(product=product,image =f.cleaned_data['image'])
						photo.save()
					except Exception as e:
						break
				return redirect(product.get_absolute_url())

	else:
			form =Productform()
			formset =imageformset(queryset=Images.objects.none())


	context ={"form":form,"formset":formset,}
	context['header'] ="Upload your products"

	return render(request, "Product/form.html",context)


def product_delete(request, slug=None):
    product = get_object_or_404(Product, slug=slug)
    product.delete() 
    return redirect('product_list')

from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Search(request):

		queryset = Product.objects.all()
		query = request.GET.get("q")   
		if query:
		    queryset = queryset.filter(
		        Q(Nom_Produit__contains=query))

		paginator = Paginator(queryset, 12)
		page = request.GET.get("page")
		try:
		    query_list = paginator.page(page)
		except PageNotAnInteger:
		    query_list = paginator.page(1)
		except EmptyPage:
		    query_list = paginator.page(paginator.num_pages)

		context = { "query_list": query_list }
		return render(request, "Product/productsearch.html", context)

from django.shortcuts import render, redirect

from .models import Images
from .forms import AdditionImageForm


def photo_list(request):
    photos = Images.objects.all()
    if request.method == 'POST':
        form = AdditionImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = AdditionImageForm()
    return render(request, 'Product/photo_list.html', {'form': form, 'photos': photos})


