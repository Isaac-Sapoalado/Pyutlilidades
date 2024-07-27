from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):

    text = models.CharField(max_length=22000)
    nome = models.CharField(max_length=200,default='(Sem Titulo)')
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_mod = models.DateTimeField(auto_now=True)
    publica = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'

class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

class Comentario(models.Model):
    
    text = models.CharField(max_length=1000)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dt_created = models.DateTimeField(auto_now_add=True)

class Interacao(models.Model):
    tipo = models.CharField(max_length=50,choices=([
            ("1","favorito"),
            ("2","gostei")]))
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tipo}--{self.blog}--{self.user.username}'

class TagBlog(models.Model):

    blog = models.ForeignKey(Blog,related_name='tags',on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag}'

    

