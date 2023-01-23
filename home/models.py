from django.db import models

# Create your models here.
class department(models.Model):
    dep_name= models.CharField(max_length=100)
    dep_description= models.TextField()

    def __str__(self):
        return self.dep_name

class architect(models.Model):
    arc_name = models.CharField(max_length=100)
    arc_spec = models.CharField(max_length=100)
    dep_name = models.ForeignKey(department, on_delete=models.CASCADE)
    arc_image = models.ImageField(upload_to='photos')

    def __str__(self):
        return 'Ar. ' + self.arc_name +  '-('+ self.arc_spec+')'


class booking(models.Model):
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=10)
    client_email = models.EmailField()
    arc_name = models.ForeignKey(architect, on_delete=models.CASCADE)
    appnt_date = models.DateField()
    booked_on = models.DateField(auto_now=True)