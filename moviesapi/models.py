
from django.db import models



# Create your models here.

class TruncatingCharField(models.CharField):
    
    def get_prep_value(self, value):
        value = super(TruncatingCharField,self).get_prep_value(value)
        if value:
            return value[:self.max_length]
        
        return self.default


class Movie(models.Model):
    Title = models.TextField()
    Year = models.TextField(default="N/A")
    Rated = models.TextField(default="N/A")
    Released = models.TextField(default="N/A")
    Runtime = models.TextField(default="N/A")
    Genre = models.TextField(default="N/A")
    Director = models.TextField(default="N/A")
    Writer = models.TextField(default="N/A")
    Actors = models.TextField(default="N/A")
    Plot = models.TextField(default="N/A")
    Language = models.TextField(default="N/A")
    Country = models.TextField(default="N/A")
    Awards = models.TextField(default="N/A")
    Poster = models.TextField(default="N/A")
    Ratings = models.TextField(default="N/A")
    Metascore = models.TextField(default="N/A")
    imdbRating = models.TextField(default="N/A")
    imdbVotes = models.TextField(default="N/A")
    imdbID = models.TextField(primary_key=True)
    Type = models.TextField(default="N/A")
    DVD = models.TextField(default="N/A")
    BoxOffice = models.TextField(default="N/A")
    Production = models.TextField(default="N/A")
    Website = models.TextField(default="N/A")
    # def __str__(self):
    #     obj = {
    #         'Title':self.Title,
    #         'Year':self.Year,
    #         'Rated':self.Rated,
    #         'Released':self.Released,
    #         'Runtime':self.Runtime,
    #         'Genre':self.Genre,
    #         'Director':self.Director,
    #         'Writer':self.Writer,
    #         'Actors':self.Actors,
    #         'Plot':self.Plot,
    #         'Language':self.Language,
    #         'Country':self.Country,
    #         'Awards':self.Awards,
    #         'Poster':self.Poster,
    #         'Ratings':self.Ratings,
    #         'Metascore':self.Metascore,
    #         'imdbRating':self.imdbRating,
    #         'imdbVotes':self.imdbVotes,
    #         'imdbID':self.imdbID,
    #         'Type':self.Type,
    #         'DVD':self.DVD,
    #         'BoxOffice':self.BoxOffice,
    #         'Production':self.Production,
    #         'Website':self.Website}
    #     # for key in keys:
    #     #     obj[key]=self[key]
    #     return json.dumps(obj)

class Comments(models.Model):
    comment = models.TextField()
    movieID = TruncatingCharField(max_length=20)
