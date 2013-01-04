from tvdash.models import Movie, Genre, SourceWebsite
from django.contrib import admin


class GenreAdmin(admin.ModelAdmin):
    pass


class MovieAdmin(admin.ModelAdmin):
    pass


class SourceWebsiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(SourceWebsite, SourceWebsiteAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)
