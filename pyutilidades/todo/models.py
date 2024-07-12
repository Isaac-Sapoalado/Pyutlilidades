from django.db import models


# Create your models here.

class Tarefa(models.Model):
    
    tarefa = models.CharField(max_length=200, null=False)
    feito = models.BooleanField(blank=False,null=False)