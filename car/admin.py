from django.contrib import admin


# Register your models here.
from car.models import washing
from car.models import detailing
from car.models import blog
from car.models import Product
from car.models import blog1, contact, feedback, query, booking1

@admin.register(washing)
class washingAdmin(admin.ModelAdmin):
	pass

@admin.register(detailing)
class detailingAdmin(admin.ModelAdmin):
	pass
	
@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    pass
    
@admin.register(blog1)
class blog1Admin(admin.ModelAdmin):
    pass
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass    
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname','phone','email','message',)

@admin.register(feedback)
class feedbackAdmin(admin.ModelAdmin):
    list_display=('name','phone','experience','comments',)

@admin.register(query)
class queryAdmin(admin.ModelAdmin):
    list_display=('name','phone','query',)

@admin.register(booking1)
class booking1Admin(admin.ModelAdmin):
    list_display=('username','userphone','useremail','usercity','selectcar','selectservice','useraddress','preferdate','prefertime','call','otherInfo',)    
