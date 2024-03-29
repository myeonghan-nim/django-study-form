from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=50)
    title_en = models.CharField(max_length=100)
    audience = models.IntegerField()
    open_date = models.DateField()
    genre = models.CharField(max_length=20)
    watch_grade = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)

    class Meta:
        ordering = ('-id', )
