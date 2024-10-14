from django.contrib import admin
from .models import Webtoon

# Register your models here.

class toonAdmin(admin.ModelAdmin):
  list_display=('title','characters')

admin.site.register(Webtoon,toonAdmin),