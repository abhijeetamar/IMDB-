from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status


class StreamPlatformAV(APIView):
    def get(self,request):
        platform=StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class WatchlistAV(APIView):
    def get(self,request):
        movies=Watchlist.objects.all()
        serializer=WatchlistSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=WatchlistSerializer(data=request.data)#'(data=request.data)'getting data from the user
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchDetailAV(APIView):
    def get(self,request,pk):
        try:
            movie=Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error':'Not found'},status=status.HTTP_404_NOT_FOUND)
        serializer=WatchlistSerializer(movie)
        return Response(serializer.data)
      
    
    def put(self,request,pk):
        movie=Watchlist.objects.get(pk=pk)
        serializer=WatchlistSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        movie =Watchlist.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformDetailAV(APIView):
    def get(self,request,pk):
        try:
            platform=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        serializer=StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self,request,pk):
        platform=StreamPlatform.objects.get(pk=pk)
        serializer=StreamPlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self,request,pk):
            platform=StreamPlatform.objects.get(pk=pk)
            platform.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        