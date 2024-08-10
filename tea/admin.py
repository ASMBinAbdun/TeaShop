from django.contrib import admin
from .models import Tea



class TeaAdmin(admin.ModelAdmin):
   list_display = ("name", "price", "quantity")

admin.site.register(Tea, TeaAdmin)
