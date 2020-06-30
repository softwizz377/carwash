from django import forms
from car.models import contact, feedback, query,  booking1
from car.models import washing
from car.models import detailing
from car.models import blog
from car.models import blog1




class contactform(forms.ModelForm):
	firstname=forms.CharField(max_length=200)
	lastname=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	message=forms.CharField(max_length=200)
	
	
	class Meta:
		model=contact
		fields="__all__"
		
		
class feedbackform(forms.ModelForm):
	experience=forms.CharField(max_length=200)
	comments=forms.CharField(max_length=200)
	name=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	
	
	
	class Meta:
		model=feedback
		fields="__all__"
		
		
class queryform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	query=forms.CharField(max_length=200)
	
	
	
	
	
	class Meta:
		model=query
		fields="__all__"
		

		
		
		
class bookingform1(forms.ModelForm):
	username=forms.CharField(max_length=200)
	userphone=forms.CharField(max_length=200)
	useremail=forms.CharField(max_length=200)
	usercity=forms.CharField(max_length=200)
	selectcar=forms.CharField(max_length=200)
	selectservice=forms.CharField(max_length=200)
	useraddress=forms.CharField(max_length=200)
	preferdate=forms.CharField(max_length=200)
	prefertime=forms.CharField(max_length=200)
	call=forms.CharField(max_length=200)
	otherInfo=forms.CharField(max_length=200)
	
	
	class Meta:
		model=booking1
		fields="__all__"

class washingform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	detail=forms.CharField(max_length=200)
	price=forms.CharField(max_length=200)
	date= forms.CharField(max_length=200)
	image = forms.ImageField()
	
	class Meta:
		db_table="washing"
	def __str__(self):
		return self.name	



class detailingform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	detail=forms.CharField(max_length=200)
	price=forms.CharField(max_length=200)
	date= forms.CharField(max_length=200)
	image = forms.ImageField()
	
	class Meta:
		db_table="detailing"
	def __str__(self):
		return self.name	


		
class blogform(forms.ModelForm):
    title= forms.CharField(max_length=200)
    detail= forms.CharField(max_length=200)
    name= forms.CharField(max_length=200)
    date= forms.CharField(max_length=200)
    photo= forms.ImageField()
    class Meta:
        db_table="blog"
    def __str__(self):
        return self.name		
		
class blog1form(forms.ModelForm):
    title= forms.CharField(max_length=200)
    detail= forms.CharField(max_length=200)
    name= forms.CharField(max_length=200)
    date= forms.CharField(max_length=200)
    photo= forms.ImageField()
    class Meta:
        db_table="blog1"
    def __str__(self):
        return self.name	

