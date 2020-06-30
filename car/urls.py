from django.contrib import admin
from django.urls import path, include
from car import views

app_name="car"

urlpatterns = [
path('carwash/', views.carwashpageview.as_view()),
path('about/', views.aboutpageview.as_view()),
path('contact/', views.contactpageview.as_view()),
path('booking/', views.bookingpageview.as_view()),
path('feedback/', views.feedbackpageview.as_view()),
path('gallary/', views.gallarypageview.as_view()),
path('washing/', views.washingpageview.as_view()),
path('services/', views.servicespageview.as_view()),
path('Product/', views.product_list),

path('detailing/', views.detailingpageview.as_view()),

path('blog1/', views.blog1pageview.as_view()),

path('blog/', views.blogpageview.as_view()),
path('query/', views.querypageview.as_view()),

path('insert',views.insert),
path('insertfeedback',views.insertfeedback),
path('insertquery',views.insertquery),

path('insertbooking1',views.insertbooking1),
path('detail/', views.cartdetailview.as_view()),
path('cartdetail/', views.cartdetailview.as_view()),
path('payment/', views.paymentview.as_view()),

]