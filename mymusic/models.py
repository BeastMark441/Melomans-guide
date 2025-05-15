from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Artist(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя исполнителя")
    slug = models.SlugField(unique=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='artists/', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    cover = models.ImageField(upload_to='albums/', blank=True, null=True)
    release_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.artist.name}"

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    title = models.CharField(max_length=200)
    track_number = models.PositiveIntegerField()
    duration = models.DurationField()

    def __str__(self):
        return f"{self.track_number}. {self.title}"

    class Meta:
        verbose_name = "Трек"
        verbose_name_plural = "Треки"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.album.title}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class UserCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'album')

    def __str__(self):
        return f"{self.user.username}'s collection: {self.album.title}"

    class Meta:
        verbose_name = "Коллекция пользователя"
        verbose_name_plural = "Коллекции пользователей" 