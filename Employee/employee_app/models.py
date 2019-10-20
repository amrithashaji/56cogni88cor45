from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255)
    image_as_a_blob = models.ImageField(upload_to = 'static/image', default = 'pic_folder/None/no-img.jpg')
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    
    def __str__(self):
        return self.employee_name

