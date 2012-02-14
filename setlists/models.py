from django.db import models
import datetime

class Song(models.Model):
  title = models.CharField(max_length=200)
  
  def __unicode__(self):
    return self.title
    
  def last_used_date(self):
    if(len(self.setlist_set.all()) > 0):
      return self.setlist_set.aggregate(models.Max('date'))['date__max']
    else:
      return None
    
  def times_used(self):
    return len(self.setlist_set.all())
    
  class Meta:
    ordering = ["title"]

class Setlist(models.Model):
  date = models.DateField()
  title = models.CharField(max_length=200)
  songs = models.ManyToManyField(Song, through='SetlistEntry')
  
  def __unicode__(self):
    return self.title
    
class SetlistEntry(models.Model):
  song = models.ForeignKey(Song)
  setlist = models.ForeignKey(Setlist)
  order = models.PositiveIntegerField()
  
  def __unicode__(self):
    return self.song.title + " in " + self.setlist.title
    
  class Meta:
    ordering = ["order"]
