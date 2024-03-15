

# Create your models here.
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    department = models.CharField(max_length=50)

    class Meta:
        app_label = 'employees'  # Set the app_label to match your app name

