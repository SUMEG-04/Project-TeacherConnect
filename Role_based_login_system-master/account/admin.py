from django.contrib import admin
from .models import User
from .models import Database
# Register your models here.
admin.site.register(User)
@admin.register(Database)
class DataAdmin(admin.ModelAdmin):
    pass