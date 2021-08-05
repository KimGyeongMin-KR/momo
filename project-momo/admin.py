from django.contrib import admin
from .models import MomoUser
# Register your models here.

class MomoUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'useremail')

admin.site.register(MomoUser, MomoUserAdmin)

