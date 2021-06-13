from copy import error
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.serializers import Serializer

from moviesapi.models import Movie, Comments
from moviesapi.serializers import MovieSerialiser, InputSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import requests
import json

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])
def movies(request):    
    if request.method == 'GET':
        possibleFilters = ['Title', 'Year','Rated','Released', 'Runtime', 'Genre','Director','Writer','Actors','Plot','Language','Country','Awards','Poster','Ratings','Metascore','imdbRating','imdbVotes','imdbID','Type','DVD','BoxOffice','Production','Website']
        args = {}
        for filter in request.data:
            if filter not in possibleFilters:
                return Response("Invalid Filter: "+filter,status=status.HTTP_400_BAD_REQUEST)
            args[filter] = request.data[filter]
        mov = Movie.objects.filter(**args)
        print(mov)
        if len(mov):
            serializer = MovieSerialiser(mov,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response("Movie not found",status=status.HTTP_200_OK)
        # if 'Title' in request.data:
        #     mov = Movie.objects.filter(Title=request.data['Title'])
        #     if len(mov):
        #         serializer = MovieSerialiser(mov[0])
        #         return Response(serializer.data,status=status.HTTP_200_OK)
        #     return Response("Movie not found",status=status.HTTP_200_OK)
        # mov = Movie.objects.all()
        # serializer = MovieSerialiser(mov,many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializers = InputSerializer(data=request.data)
        if serializers.is_valid():
            movieReq = requests.get('http://www.omdbapi.com/?i=tt3896198&apikey=861e4517', params={'t':serializers.data['Title']})
            if not movieReq:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            content = json.loads(movieReq.content)
            if content['Response']=="False":
                return Response(movieReq.content, status=status.HTTP_200_OK)
            for x in content:
                if type(content[x]) is not str:
                    content[x] = json.dumps(content[x])
            serializers = MovieSerialiser(data=content)
            if(serializers.is_valid()):
                serializers.save()
                return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(serializers.errors,status=status.HTTP_200_OK)
            # return Response(serializers.data, status=status.HTTP_200_OK)
            return Response(movieReq.content, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def comments(request):
    if request.method=='GET':
        possibleFilters = ['movieID']
        args = {}
        for filter in request.data:
            if filter not in possibleFilters:
                return Response("Invalid key: "+filter,status=status.HTTP_400_BAD_REQUEST)
            args[filter] = request.data[filter]
        comments = Comments.objects.filter(**args)

        if len(comments):
            serializer = CommentSerializer(comments,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response("comment not found",status=status.HTTP_200_OK)

        comments = Comments.objects.all()
        commentSerializer = CommentSerializer(comments,many=True)
        return Response(commentSerializer.data,status=status.HTTP_200_OK)
    if request.method=='POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            checking = Movie.objects.filter(imdbID=request.data['movieID'])
            if len(checking):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response("Movie not found in database", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)