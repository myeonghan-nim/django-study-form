from django.shortcuts import render, redirect, get_object_or_404

from .forms import MovieForm, MovieModelForm, CommentForm
from .models import Movie, Comment

# Create your views here.


def index(request):

    movies = Movie.objects.all().order_by('-id')

    context = {
        'movies': movies,
    }

    return render(request, 'index.html', context)


def detail(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)
    comment_form = CommentForm()

    context = {
        'movie': movie,
        'comment_form': comment_form,
    }

    return render(request, 'detail.html', context)


def create(request):

    if request.method == 'POST':
        form = MovieForm(request.POST)
    
        if form.is_valid():
            movie = Movie()

            movie.title = form.cleaned_data.get('title')
            movie.title_en = form.cleaned_data.get('title_en')
            movie.audience = form.cleaned_data.get('audience')
            movie.open_date = form.cleaned_data.get('open_date')
            movie.genre = form.cleaned_data.get('genre')
            movie.watch_grade = form.cleaned_data.get('watch_grade')
            movie.score = form.cleaned_data.get('score')
            movie.poster_url = form.cleaned_data.get('poster_url')
            movie.description = form.cleaned_data.get('description')

            movie.save()

            return redirect('movies:index')
    else:
        form = MovieForm()

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)


def create_model_form(request):

    if request.method == 'POST':
        form = MovieModelForm(request.POST)

        if form.is_valid():
            movie = form.save()

            return redirect('movies:detail', movie.id)
    else:
        form = MovieModelForm()

    context ={
        'form': form,
    }

    return render(request, 'form.html', context)


def delete(request, movie_id):
    
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        movie.delete()

        return redirect('movies:index')
    else:

        return redirect('movies:detail', movie_id)


def update(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():

            movie.title = form.cleaned_data.get('title')
            movie.title_en = form.cleaned_data.get('title_en')
            movie.audience = form.cleaned_data.get('audience')
            movie.open_date = form.cleaned_data.get('open_date')
            movie.genre = form.cleaned_data.get('genre')
            movie.watch_grade = form.cleaned_data.get('watch_grade')
            movie.score = form.cleaned_data.get('score')
            movie.poster_url = form.cleaned_data.get('poster_url')
            movie.description = form.cleaned_data.get('description')

            movie.save()

            return redirect('movies:detail', movie_id)
    else:
        form = MovieForm(initial=movie.__dict__)

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)


def update_model_form(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=movie)

        if form.is_valid():
            form.save()

            return redirect('movies:detail', movie_id)
    else:
        form = MovieModelForm(instance=movie)
    
    context = {
        'form': form,
    }

    return render(request, 'form.html', context)


def comment_create(request, movie_id):

    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie

            comment.save()

            return redirect('movies:detail', movie_id)
