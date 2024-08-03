from django.db import models
# Create your models here.

class Materia(models.Model):
    materia = models.CharField(max_length=500,unique=True)

    def __str__(self):
      return self.materia


class Assunto(models.Model):
    
    assunto = models.CharField(max_length=500,unique=True)
    materia = models.ForeignKey(Materia,on_delete=models.CASCADE)

    def __str__(self):
      return f'{self.assunto},{self.materia}'

class Banca(models.Model):
   
    banca = models.CharField(max_length=500,unique=True)

    def __str__(self):
      return self.banca


class Questao(models.Model):

    questao = models.CharField(max_length=5000,unique=True)
    banca = models.ForeignKey(Banca,on_delete=models.CASCADE)
    assunto = models.ForeignKey(Assunto,on_delete=models.CASCADE)
    concurso = models.CharField(max_length=500)

    def __str__(self):
      return self.questao

class Alternativa(models.Model):
   
    alternativa = models.CharField(max_length=500)
    certo = models.BooleanField()
    questao = models.ForeignKey(Questao,related_name='alternativa',on_delete=models.CASCADE)

    def __str__(self):
      return f'{self.alternativa}--{self.certo}'


Questao.save_base