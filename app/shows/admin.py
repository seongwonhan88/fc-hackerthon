from django.contrib import admin

from .models import Show, Comment, ShowPick, Rating

admin.site.register(Show)
admin.site.register(Comment)
admin.site.register(ShowPick)
admin.site.register(Rating)
