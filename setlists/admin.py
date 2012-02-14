from setlists.models import Setlist, Song, SetlistEntry
from django.contrib import admin

class SetlistEntryInline(admin.TabularInline):
  model = SetlistEntry
  extra = 1
  
class SetlistAdmin(admin.ModelAdmin):
  inlines = (SetlistEntryInline, )
  
class SongAdmin(admin.ModelAdmin):
  inlines = (SetlistEntryInline, )
  list_display = ['title', 'times_used', 'last_used_date']
  
admin.site.register(Setlist, SetlistAdmin)
admin.site.register(Song, SongAdmin)
