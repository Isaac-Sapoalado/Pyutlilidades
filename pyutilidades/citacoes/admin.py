from django.contrib import admin
from .models import Citacao
# Register your models here.
@admin.register(Citacao)
class CitacaoAdmin(admin.ModelAdmin):
    fields = ['citacao','autor']