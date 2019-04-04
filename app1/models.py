from django.db import models

# Create your models here.
class UserRole(models.Model):
    role_id=models.AutoField(primary_key=True)
    role_name=models.CharField(max_length=225, default="",unique=True )
