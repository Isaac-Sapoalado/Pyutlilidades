from django.contrib import admin
from .models import Palavra,Dica
# Register your models here.
class Dicainline(admin.TabularInline):
    model = Dica
    extra = 0

@admin.register(Palavra)
class Palavraadmin(admin.ModelAdmin):
    fields = ['palavra']
    inlines = [Dicainline]