from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarefa(models.Model):
    
    tarefa = models.CharField(max_length=200, null=False)
    feito = models.BooleanField(blank=False,null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)