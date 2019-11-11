from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),

    path('create/', views.create, name='create'),

    path('<int:movie_id>/delete/', views.delete, name='delete'),

    path('<int:movie_id>/update/', views.update, name='update'),

    path('create-model-form/', views.create_model_form, name='create_modelform'),
    path('<int:movie_id>/update-model-form', views.update_model_form, name='update_modelform'),

    path('<int:movie_id>/comments/create/', views.comment_create, name='comment_create'),
]
