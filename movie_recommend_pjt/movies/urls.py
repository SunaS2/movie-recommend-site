from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.get_movies),
    path('movies/<int:movie_pk>/wish-movie/', views.wish_movie),
    path('movies/wish-movie/', views.logined_wish_movie_list),
    path('movies/genres-list/', views.genres_list),
    path('movies/otts-list/', views.otts_list),
    path('movies/<int:movie_pk>/comments/', views.comment_create),
    path('movies/list/', views.comment_list_user),
    path('movies/list/<int:movie_pk>/', views.comment_list_movie),
]
