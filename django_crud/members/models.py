from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True,error_messages={'unique':'Email is already used'})
    phone = models.IntegerField(null=True, unique=True, error_messages={'unique':'Phone is already used'})
    joined_date = models.DateTimeField(blank=False, auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
