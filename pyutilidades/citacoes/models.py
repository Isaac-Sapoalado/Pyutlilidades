from django.db import models

# Create your models here.

class Citacao(models.Model):

    citacao = models.CharField(max_length=1800)
    autor = models.CharField(max_length=100)