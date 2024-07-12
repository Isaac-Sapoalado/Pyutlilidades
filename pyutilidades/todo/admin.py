from django.contrib import admin
from .models import Tarefa

# Register your models here.
@admin.register(Tarefa)
class Tarefa_Admin(admin.ModelAdmin):
    list_display = ['tarefa', 'feito']
