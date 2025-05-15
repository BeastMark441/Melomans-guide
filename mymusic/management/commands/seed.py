from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mymusic.models import Artist, Album, Track, News, Review
from django.utils import timezone
from django.utils.text import slugify
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Наполняет базу тестовыми артистами, альбомами, треками, новостями и отзывами.'

    def handle(self, *args, **kwargs):
        # Артисты
        artists = []
        artist_names = [
            'Ария', 'Кино', 'ДДТ', 'Земфира', 'Сплин', 'Мумий Тролль', 'Би-2', 'Ленинград', 'Чайф', 'Ночные Снайперы'
        ]
        for name in artist_names:
            base_slug = slugify(name)
            slug = base_slug
            counter = 1
            while Artist.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            
            artist = Artist.objects.create(
                name=name,
                slug=slug,
                bio=f'Биография {name}',
            )
            artists.append(artist)
        self.stdout.write(self.style.SUCCESS(f'Создано артистов: {len(artists)}'))

        # Альбомы
        albums = []
        for artist in artists:
            for i in range(1, 3):
                album, created = Album.objects.get_or_create(
                    title=f'Альбом {i} {artist.name}',
                    artist=artist,
                    defaults={
                        'release_date': timezone.now().date(),
                        'description': f'Описание альбома {i} группы {artist.name}',
                    }
                )
                albums.append(album)
        self.stdout.write(self.style.SUCCESS(f'Создано альбомов: {len(albums)}'))

        # Треки
        tracks = []
        for album in albums:
            for i in range(1, 6):
                # Генерируем случайную длительность от 2 до 6 минут
                minutes = random.randint(2, 6)
                seconds = random.randint(0, 59)
                duration = timedelta(minutes=minutes, seconds=seconds)
                
                track, created = Track.objects.get_or_create(
                    album=album,
                    track_number=i,
                    defaults={
                        'title': f'Трек {i} из {album.title}',
                        'duration': duration,
                    }
                )
                tracks.append(track)
        self.stdout.write(self.style.SUCCESS(f'Создано треков: {len(tracks)}'))

        # Новости
        news_list = []
        for i in range(1, 6):
            news, created = News.objects.get_or_create(
                title=f'Новость {i}',
                defaults={
                    'content': f'Текст новости {i}',
                    'created_at': timezone.now(),
                }
            )
            news_list.append(news)
        self.stdout.write(self.style.SUCCESS(f'Создано новостей: {len(news_list)}'))

        # Пользователь для отзывов
        user, _ = User.objects.get_or_create(username='testuser')

        # Отзывы
        reviews = []
        for album in albums:
            for i in range(2):
                review, created = Review.objects.get_or_create(
                    user=user,
                    album=album,
                    defaults={
                        'rating': random.randint(3, 5),
                        'text': f'Отзыв {i+1} к альбому {album.title}',
                        'created_at': timezone.now(),
                    }
                )
                reviews.append(review)
        self.stdout.write(self.style.SUCCESS(f'Создано отзывов: {len(reviews)}'))

        self.stdout.write(self.style.SUCCESS('База успешно наполнена тестовыми данными!')) 