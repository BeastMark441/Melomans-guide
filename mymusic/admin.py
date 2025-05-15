from django.contrib import admin
from .models import Artist, Album, Track, Review, News, UserCollection

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_date')
    list_filter = ('artist', 'release_date')
    search_fields = ('title', 'artist__name')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'track_number', 'duration')
    list_filter = ('album',)
    search_fields = ('title', 'album__title')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'album', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'album__title')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

@admin.register(UserCollection)
class UserCollectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'album', 'added_at')
    list_filter = ('user', 'added_at')
    search_fields = ('user__username', 'album__title') 