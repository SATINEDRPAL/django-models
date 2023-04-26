from django.db import models

# Create your models here.
# class contactdata(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField(max_length=100)
#     subject=models.CharField(max_length=200)
#     message=models.CharField(max_length=500)
class employee(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField(max_length=10)
    Email=models.EmailField(max_length=100)
    Mobile_no=models.IntegerField(max_length=100)

    
    def __str__(self):
        return self.Name