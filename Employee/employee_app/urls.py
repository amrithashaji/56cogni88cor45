from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('add_employee/', views.add_employee, name='add_employee'),
    
    #path('post/', views.individual_post, name='individual_post')
]