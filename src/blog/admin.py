from django.contrib import admin
from blog.models import Tag, Category, Page, Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name',),
    }

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('name',),
    }

@admin.register(Page)
class PageAdmin(SummernoteModelAdmin):
    list_display = 'id', 'title', 'is_published',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'is_published',
    list_per_page = 50
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',),
    }
    summernote_fields = 'content',

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = 'id', 'title', 'is_published','created_by'
    list_display_links = 'title',
    search_fields = 'id', 'title', 'is_published','slug', 'excerpt', 'content',
    list_filter = 'category', 'is_published',
    list_editable = 'is_published',
    list_per_page = 50
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('title',),
    }
    autocomplete_fields = 'category', 'tags',
    readonly_fields = 'created_at', 'created_by', 'updated_at', 'updated_by',
    summernote_fields = 'content',

    def save_model(self, request, obj: Post, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
            obj.updated_by = request.user
        return super().save_model(request, obj, form, change)