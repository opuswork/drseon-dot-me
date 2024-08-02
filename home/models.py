from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="Enter the category! (ex:Article)")

    def __str__(self):
        return self.name
    
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
		.filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Publish'),
    )
    title = models.CharField(max_length=250)
    title_image = models.ImageField(blank=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ManyToManyField(Category, help_text="Set the category!")
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.
    tags = TaggableManager()
    
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def is_content_more300(self):
        return len(self.body) > 300
    
    def get_content_under300(self):
        return self.body[:300]
    
    def get_absolute_url(self):
        url = reverse('blog:blog_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
        return f'{url}?menu=blog'    
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'

class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class ContactMessage(models.Model):
    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField()
    sender_phone = models.CharField(max_length=15, blank=True, null=True)
    sender_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender_name    