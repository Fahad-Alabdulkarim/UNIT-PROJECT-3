from django.contrib import admin
from .models import User

# Register your models here.




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_shared_user', 'is_staff')
    list_filter = ('is_shared_user', 'is_staff')