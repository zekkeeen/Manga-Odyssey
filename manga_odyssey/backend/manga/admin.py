from django.contrib import admin
from .models import Manga

@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'release_year')
    search_fields = ('title', 'author', 'genre')

# Register your models here.
