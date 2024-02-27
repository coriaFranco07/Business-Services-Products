from django.contrib import admin
from .models import Nosotros, Ubicacion

# Register your models here.

class NosotrosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class UbucacionAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
admin.site.register(Nosotros, NosotrosAdmin)
    
admin.site.register(Ubicacion, UbucacionAdmin)
