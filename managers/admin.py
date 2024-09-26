from django.contrib import admin
from accounts.models import User

# Enregistrer un manager via l'admin
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_manager')
    list_filter = ('is_manager',)
    
    def save_model(self, request, obj, form, change):
        obj.is_manager = True  # Assure que is_manager est toujours vrai pour les managers
        super().save_model(request, obj, form, change)


