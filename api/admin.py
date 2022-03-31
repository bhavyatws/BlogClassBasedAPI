from django.contrib import admin
from api.models import Category, Post,Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','body','owner','created']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['id','body','owner','post','created']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','owner']