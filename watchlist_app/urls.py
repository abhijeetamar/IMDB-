from django.urls import path
from watchlist_app.views import *

urlpatterns=[
    path('',WatchlistAV.as_view(),name='watch_list'),
    path('<int:pk>',WatchDetailAV.as_view(),name='watch-detail'),
    path('stream',StreamPlatformAV.as_view(),name='stream'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-detail'),
]