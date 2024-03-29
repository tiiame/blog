from django.contrib import admin
from .models import BaseModel, Profile, Skill, About, Category, Post, Service, Portfolio,Blog
# Register your models here.

# admin.site.register(BaseModel)

@admin.register(BaseModel)
class BaseModel(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at',)


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('full_name', 'image', 'bio')
    list_display_links = ('full_name',)
    search_fields = ('full_name',)

@admin.register(Skill)
class Skill(admin.ModelAdmin):
    list_display = ('title', 'percentage', 'order')
    list_display_links = ('title',)
    search_fields = ('order',)


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('experience', 'total_projects', 'total_users', 'salary')
    list_display_links = ('total_projects','total_users')
    search_fields = ('total_projects',)
    list_filter = ('salary',)


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('author', 'image', 'description', 'title', 'count_views','id',)
    list_display_links = ('author','title')
    search_fields = ('title',)
    list_filter = ('count_views',)

@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ('title', 'icon', 'description')
    list_display_links = ('title',)
    search_fields = ('title',)    


@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'link', 'category', 'complated_at',)
    list_display_links = ('link','category')
    search_fields = ('title','category',)
 
@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'created_at','category',)
    list_display_links = ('title',)
    search_fields = ('title',)
