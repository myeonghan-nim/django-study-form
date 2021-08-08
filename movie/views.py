from django.shortcuts import render, redirect, get_object_or_404

from .forms import MovieModelForm, CommentForm
from .models import Movie, Comment


def index(request):
    context = {
        'movies': Movie.objects.all().order_by('-id'),
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    context = {
        'movie': get_object_or_404(Movie, id=movie_id),
        'comment_form': CommentForm(),
    }
    return render(request, 'detail.html', context)


def create_model_form(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie:detail', movie.id)
    else:
        form = MovieModelForm()
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
            return redirect('movie:detail', movie_id)
    else:
        form = MovieModelForm(instance=movie)
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)


def delete(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie:index')
    else:
        return redirect('movie:detail', movie_id)


def comment_create(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.save()
            return redirect('movie:detail', movie_id)
