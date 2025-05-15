from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<slug:slug>/', views.artist_detail, name='artist_detail'),
    path('albums/', views.album_list, name='album_list'),
    path('albums/<int:pk>/', views.album_detail, name='album_detail'),
    path('albums/<int:album_id>/review/', views.add_review, name='add_review'),
    path('albums/<int:album_id>/add-to-collection/', views.add_to_collection, name='add_to_collection'),
    path('albums/<int:album_id>/remove-from-collection/', views.remove_from_collection, name='remove_from_collection'),
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('my-collection/', views.my_collection, name='my_collection'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 