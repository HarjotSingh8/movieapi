# serializers.py
from rest_framework import serializers

from .models import Movie, Comments

class InputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ['Title']
        # fields = ('Title', 'Year','Rated','Released', 'Runtime', 'Genre','Director','Writer','Actors','Plot')

class MovieSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        # fields = ['Title']
        fields = ('Title', 'Year','Rated','Released', 'Runtime', 'Genre','Director','Writer','Actors','Plot','Language','Country','Awards','Poster','Ratings','Metascore','imdbRating','imdbVotes','imdbID','Type','DVD','BoxOffice','Production','Website')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ['movieID','comment']
        # fields = ('Title', 'Year','Rated','Released', 'Runtime', 'Genre','Director','Writer','Actors','Plot')
