from django.contrib import admin

# Register your models here.

from post.models import Post, Category, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)

