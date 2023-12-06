from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from apps.models import Cities, Stocks, Fruits

# admin.site.register(Cities)
admin.site.register(Stocks)
admin.site.register(Fruits)

@admin.register(Cities)
class Region(ImportExportModelAdmin):
    pass
