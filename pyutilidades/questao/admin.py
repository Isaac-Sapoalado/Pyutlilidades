from django.contrib import admin
from .models import Materia,Assunto,Banca,Questao,Alternativa
# Register your models here.

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    fields = ['materia']

@admin.register(Assunto)
class AssuntoAdmin(admin.ModelAdmin):
    fields = ['assunto','materia']

@admin.register(Banca)
class BancaAdmin(admin.ModelAdmin):
    fields = ['banca']

class Alternativainline(admin.TabularInline):
    model = Alternativa
    extra = 4
    max_num = 5

@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    fields = ['questao','banca','assunto','concurso']
    inlines = [Alternativainline]
