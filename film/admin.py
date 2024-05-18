from django.contrib import admin
from .models import Films, Director, Genre, Rate
from authentication.models import User
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
# Register your models here.

class FilmsCategoryResource(resources.ModelResource):
    
    def get_direct(self, film):
        return ', '.join([str(direct) for direct in film.direct.all()])
    
    def dehydrate_direct(self,film):
        return self.get_direct(film)
    
    def get_genre(self,film):
        return ", ".join([str(genre) for genre in film.genre.all()])

    def dehydrate_genre(self, film):
        return self.get_genre(film)
    
    def dehydrate_is_favorite(self, film):
        return 'Избранное' if film.is_favorite else 'Не избранное'


    class Meta:
        model = Films
        fields = ('id', 'title', 'is_favorite', 'genre', 'subtitle', 'year', 'rating_stars', 'direct') 
    

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display=('first_name', 'last_name', 'email')
    fieldsets = (
        ("Контактная информация", {"fields": ['first_name', 'last_name', 'email']}),
    )
    

class FilmsCategory(ImportExportModelAdmin):
    resource_class=FilmsCategoryResource
    list_display = ('id','title', 'get_genre')
    list_filter = ['direct','genre']
    list_display_links=['title']
    fields = ('title',  'direct', 'genre')

    def get_export_queryset(self, request):
        queryset=super().get_export_queryset(request)
        queryset=queryset.filter(is_favorite=True)
        return queryset
    
  

class DirectorId(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Films, FilmsCategory)
admin.site.register(Director, DirectorId)
admin.site.register(Genre)
admin.site.register(Rate)