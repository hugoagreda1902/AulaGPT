from django.contrib import admin
from .models import User  # Asegúrate de que sea 'User', no 'Usuario'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'surname', 'email', 'role')
    search_fields = ('name', 'surname', 'email')
    list_filter = ('role',)
