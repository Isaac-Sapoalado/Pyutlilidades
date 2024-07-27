from django.contrib import admin
from .models import Blog,TagBlog,Comentario,Interacao,Tag
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ['nome','text','publica','user']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ['tag']

@admin.register(TagBlog)
class TagBlogAdmin(admin.ModelAdmin):
    fields = ['blog','tag']

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    fields = ['text','blog','user']

@admin.register(Interacao)
class InteracaoAdmin(admin.ModelAdmin):
    fields = ['tipo','blog','user']
