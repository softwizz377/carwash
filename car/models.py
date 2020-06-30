from django.db import models

# Create your models here.
class contact(models.Model):
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	message=models.CharField(max_length=200)
	
	class Meta:
		db_table="contact"
		
	def __str__(self):
		return self.name
		


class feedback(models.Model):
	experience=models.CharField(max_length=200)
	comments=models.CharField(max_length=200)
	name=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	
	class Meta:
		db_table="feedback"
		
	def __str__(self):
		return self.name
		
		
class query(models.Model):
	name=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	query=models.CharField(max_length=200)
	
	
	class Meta:
		db_table="query"
		
	def __str__(self):
		return self.name
				
				
				
				

				

				
				
class booking1(models.Model):
	username=models.CharField(max_length=200)
	userphone=models.CharField(max_length=200)
	useremail=models.CharField(max_length=200)
	usercity=models.CharField(max_length=200)
	selectcar=models.CharField(max_length=200)
	selectservice=models.CharField(max_length=200)
	useraddress=models.CharField(max_length=200)
	preferdate=models.CharField(max_length=200)
	prefertime=models.CharField(max_length=200)
	call=models.CharField(max_length=200)
	otherInfo=models.CharField(max_length=200)
    
	
	
	class Meta:
		db_table="booking1"
		
	def __str__(self):
		return self.name
		

class washing(models.Model):
	name=models.CharField(max_length=200)
	detail=models.CharField(max_length=200)
	price=models.CharField(max_length=200)
	date= models.CharField(max_length=200)
	image = models.ImageField(upload_to = 'images/')
	
	class Meta:
		db_table="washing"
	def __str__(self):
		return self.name
		
class detailing(models.Model):
	name=models.CharField(max_length=200)
	detail=models.CharField(max_length=200)
	price=models.CharField(max_length=200)
	date= models.CharField(max_length=200)
	image = models.ImageField(upload_to = 'images/')
	
	class Meta:
		db_table="detailing"
	def __str__(self):
		return self.name
		
class blog(models.Model):
    title= models.CharField(max_length=200)
    detail= models.CharField(max_length=2000)
    name= models.CharField(max_length=200)
    date= models.CharField(max_length=200)
    photo= models.ImageField(upload_to ='images/')
    class Meta:
        db_table="blog"
    def __str__(self):
        return self.name		

class blog1(models.Model):
    title= models.CharField(max_length=200)
    detail= models.CharField(max_length=2000)
    name= models.CharField(max_length=200)
    date= models.CharField(max_length=200)
    photo= models.ImageField(upload_to ='images/')
    class Meta:
        db_table="blog1"
    def __str__(self):
        return self.name
class Product(models.Model):
    
    name= models.CharField(max_length=100, db_index=True)

    price=models.DecimalField(max_digits=10, decimal_places=2)
    
    photo= models.ImageField(upload_to ='products/', blank=True)
    
    class Meta:
        db_table="Product"
    def __str__(self):
        return self.name			