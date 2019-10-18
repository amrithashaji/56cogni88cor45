from django.db import models
# from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User
# from django.urls import reverse


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    image_as_a_blob = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=20)
    phone = models.IntegerField()
    address = models.TextField()
    
    def __str__(self):
        return self.employee_name
