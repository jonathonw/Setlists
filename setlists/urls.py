from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from setlists.models import Setlist, Song
from django.db import models

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Song.objects.annotate(times_used=models.Count('setlist')).order_by('-times_used')[:5],
            context_object_name='most_frequently_used_songs',
            template_name='setlists/index.html')),
    url(r'^all/$',
        ListView.as_view(
            queryset=Setlist.objects.order_by('-date'),
            context_object_name='all_setlists',
            template_name='setlists/all.html')),
    url(r'^setlist/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Setlist,
            template_name='setlists/setlist.html')),
    url(r'^stats/$',
        ListView.as_view(
            queryset=Song.objects.annotate(times_used=models.Count('setlist'), last_used=models.Max('setlist__date')).order_by('-times_used', '-last_used', 'title'),
            context_object_name='songs',
            template_name='setlists/stats.html')),
)
