from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework import mixins //
from rest_framework import generics
# from models import *
from watchlist_app.models import *
from django.http import JsonResponse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class StreamPlatfromViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamingPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = StreamingPlatformSerializer(user)
        return Response(serializer.data)
    
    
class WatchListAV(APIView):
    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
class WatchListDetail(APIView):
    def get(self,request,pk): 
        try:
            movie=WatchList.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie)
        return Response(serializer.data)
    
    def post(self,request,pk):
        try:
            movie=WatchList.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=401)
    
    def delete(self,request,pk):
        try:
            movie=WatchList.objects.get(id=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=204)

class ReviewCreate(generics.CreateAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer 
    def perform_create(self,serializer):
        pk=self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=pk)
        
class ReviewList(generics.ListCreateAPIView):
    serializer_class=ReviewSerializer
    def get_queryset(self):
        pk=self.kwargs['pk']
        watchlist = WatchList.objects.get(id=pk)
        return Review.objects.filter(watchlist=pk)
    def perform_create(self,serializer):
        pk=self.kwargs['pk']
        watchlist = WatchList.objects.get(id=pk)
        
        serializer.save(watchlist=watchlist)
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

# class StreamingPlatformAV(APIView):
#     def get(self,request):
#         platforms=StreamPlatform.objects.all()
#         serializer=StreamingPlatformSerializer(platforms,many=True,context={'request': request})
#         return Response(serializer.data)
#     def post(self,request):
#         serializer=StreamingPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class StreamingPlatformDetailAV(APIView):
#     def get(self,request,pk): 
#         try:
#             platform=StreamPlatform.objects.get(id=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer=StreamingPlatformSerializer(platform,context={'request': request})
#         return Response(serializer.data)
    
#     def post(self,request,pk):
#         try:
#             platform=StreamPlatform.objects.get(id=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer=StreamingPlatformSerializer(platform,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(status=401)
    
#     def delete(self,request,pk):
#         try:
#             platform=StreamPlatform.objects.get(id=pk)
#         except:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         platform.delete()
#         return Response(status=204)
    























# @api_view(['GET','POST'])
# def movies_list(request):
#     if request.method=='POST':
#         serializer=WatchListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(status=401)
#     if request.method=='GET':
#         movies=Movie.objects.all()
#         serializer=WatchListSerializer(movies,many=True)
#         return Response(serializer.data)
# @api_view(['GET',"PUT","DELETE"])
# def movie_detail(request,pk):
#     try:
#         movie=Movie.objects.get(id=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method=='GET':
#         serializer=WatchListSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method=='PUT':
#         serializer=WatchListSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(status=401)
    
#     if request.method=='DELETE':
#         movie.delete()
#         return Response(status=204)
#class ReviewDetail(mixins.RetrieveModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
# class ReviewtList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)