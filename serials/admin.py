from django.contrib import admin
from .models import Serials
from film.models import Director, Genre
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class SerialsCategory(ImportExportModelAdmin):
    list_display = ('id','title', 'get_genre')
    list_filter = ['director','genre']
    list_display_links=['title']

admin.site.register(Serials, SerialsCategory)

