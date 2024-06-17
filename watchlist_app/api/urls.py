# from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('stream',StreamPlatfromViewset,basename='streamplatform')
urlpatterns = [
    path('list',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',WatchListDetail.as_view(),name='movie-detail'),
    # path('platform/',StreamPlatfromViewset.as_view(),name='streaming-platforms-list'),
    # path('platform/<int:pk>',StreamPlatfromViewset.as_view(),name='streamplatform-detail'),
    path('',include(router.urls)),
     path('<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    path('<int:pk>/review',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    
]
