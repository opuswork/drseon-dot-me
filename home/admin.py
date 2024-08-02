from django.contrib import admin
from .models import Category, Post, Comment, Subscription, ContactMessage
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    # Apply summernote to content field of your model
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    summernote_fields = ('body',)

class CommentAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created','active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
    summernote_fields = ('body',)    

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender_email', 'sender_phone', 'created_at')
    search_fields = ('sender_name', 'sender_email', 'sender_message')

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    list_filter = ('subscribed_at',)

# Register your models here.
admin.site.site_header = "Dr.Seon Admin Dashboard"
admin.site.site_title = "Dr.Seon Admin Dashboard"
admin.site.index_title = "Dr.Seon Admin Dashboard"
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
