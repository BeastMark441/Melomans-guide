from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .models import Artist, Album, Track, Review, News, UserCollection
from .forms import UserRegisterForm
from django.db.models import Avg

def home(request):
    latest_albums = Album.objects.select_related('artist').all().order_by('-release_date')[:6]
    latest_news = News.objects.all().order_by('-created_at')[:3]
    top_artists = Artist.objects.annotate(avg_rating=Avg('albums__reviews__rating')).order_by('-avg_rating')[:5]
    
    context = {
        'latest_albums': latest_albums,
        'latest_news': latest_news,
        'top_artists': top_artists,
    }
    return render(request, 'mymusic/home.html', context)

def artist_list(request):
    artists = Artist.objects.all().order_by('name')
    return render(request, 'mymusic/artist_list.html', {'artists': artists})

def artist_detail(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    albums = artist.albums.all().order_by('-release_date')
    return render(request, 'mymusic/artist_detail.html', {
        'artist': artist,
        'albums': albums
    })

def album_list(request):
    albums = Album.objects.all().order_by('-release_date')
    return render(request, 'mymusic/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    tracks = album.tracks.all().order_by('track_number')
    reviews = album.reviews.all().order_by('-created_at')
    return render(request, 'mymusic/album_detail.html', {
        'album': album,
        'tracks': tracks,
        'reviews': reviews
    })

@login_required
def add_review(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        text = request.POST.get('text')
        Review.objects.create(
            user=request.user,
            album=album,
            rating=rating,
            text=text
        )
        messages.success(request, 'Ваш отзыв успешно добавлен!')
        return redirect('album_detail', pk=album_id)
    return render(request, 'mymusic/add_review.html', {'album': album})

@login_required
def add_to_collection(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    UserCollection.objects.get_or_create(user=request.user, album=album)
    messages.success(request, f'Альбом {album.title} добавлен в вашу коллекцию!')
    return redirect('album_detail', pk=album_id)

@login_required
def remove_from_collection(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    UserCollection.objects.filter(user=request.user, album=album).delete()
    messages.success(request, f'Альбом {album.title} удален из вашей коллекции!')
    return redirect('my_collection')

def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'mymusic/news_list.html', {'news': news})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'mymusic/news_detail.html', {'news': news})

@login_required
def my_collection(request):
    collection = UserCollection.objects.filter(user=request.user).select_related('album')
    return render(request, 'mymusic/my_collection.html', {'collection': collection})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Аккаунт успешно создан!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form}) 