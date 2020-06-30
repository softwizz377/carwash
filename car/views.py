from django.shortcuts import render, redirect
from car.models import contact, feedback, query,  booking1,washing,detailing,blog,blog1,Product
from car.forms import contactform, feedbackform, queryform,  bookingform1,washingform,detailingform,blogform,blog1form
from django.contrib.auth.models import User
from django.views.generic import TemplateView,ListView
from cart.forms import CartAddProductForm
# Create your views here.

class carwashpageview(TemplateView):
	template_name="carwash.html"
class aboutpageview(TemplateView):
	template_name="about.html"
class contactpageview(TemplateView):
	template_name="contact.html"
class bookingpageview(TemplateView):
	template_name="booking.html"
class feedbackpageview(TemplateView):
	template_name="feedback.html"
class querypageview(TemplateView):
	template_name="query.html"
class gallarypageview(TemplateView):
	template_name="gallary.html"

class washingpageview(ListView):
	template_name="washing.html"
	def get_queryset(self):
	 return washing.objects.all()
class servicespageview(TemplateView):
	template_name="services.html"
class detailingpageview(ListView):
	template_name="detailing.html"
	def get_queryset(self):
	 return detailing.objects.all()

class blogpageview(ListView):
	template_name="blog.html"
	def get_queryset(self):
	 return blog.objects.all()
class blog1pageview(ListView):
	template_name="blog1.html"
	def get_queryset(self):
	 return blog1.objects.all()
class cartdetailview(TemplateView):
	template_name="cartdetail.html"
class paymentview(TemplateView):
	template_name="payment.html"
def insert(request):
	if request.method=='POST':
		form=contactform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/contact/')
			except:
				pass
	else:
		form=contactform()
	return render(request,'contact.html',{'form':form})

	
	
	
def insertfeedback(request):
	if request.method=='POST':
		form=feedbackform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/feedback/')
			except:
				pass
	else:
		form=feedbackform()
	return render(request,'feedback.html',{'form':form})

	
	
	
def insertquery(request):
	if request.method=='POST':
		form=queryform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/query/')
			except:
				pass
	else:
		form=queryform()
	return render(request,'query.html',{'form':form})
	
	
	


	
	
	
def insertbooking1(request):
	if request.method=='POST':
		form=bookingform1(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/booking/')
			except:
				pass
	else:
		form=bookingform1()
	return render(request,'booking.html',{'form':form})

def product_list(request):
	products=Product.objects.all()
	cart_product_form=CartAddProductForm()
	context={
		'products':products,
		'cart_product_form':cart_product_form
	}
	return render(request,'Product.html',context)

