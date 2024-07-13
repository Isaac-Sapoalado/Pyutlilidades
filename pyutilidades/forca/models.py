from django.db import models

# Create your models here.

class Palavra(models.Model):
    palavra = models.CharField(max_length=100)

class Dica(models.Model):
    dica = models.CharField(max_length=1000)
    palavra = models.ForeignKey(Palavra,related_name='dicas',on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.dica
