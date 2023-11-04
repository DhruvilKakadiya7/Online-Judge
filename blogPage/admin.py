from django.contrib import admin
from .models import Like, Dislike, Comment
# Register your models here.
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Comment)