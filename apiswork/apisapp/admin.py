from django.contrib import admin
from .models import Workapi


# Register your models here.
class workapiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tittle')
    list_display_links = ('name','tittle')
    search_fields = ('name','tittle','description')


admin.site.register(Workapi, workapiAdmin)
