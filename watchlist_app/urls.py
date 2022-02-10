from django.urls import path
from watchlist_app.views import *

urlpatterns=[
    path('',MovieListAV.as_view(),name='movie_list'),
    path('<int:pk>',MovieDetailAv.as_view(),name='movie-detail'),
]