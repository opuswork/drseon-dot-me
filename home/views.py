from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.views.generic import ListView
from .models import Post, Comment
#from .forms import EmailPostForm, CommentForm, SubscriptionForm
from .forms import SubscriptionForm, ContactForm
from .models import Subscription, ContactMessage
from taggit.models import Tag
from django.contrib import messages
import logging
# Create your views here.
def home(request):
    menu = request.GET.get('menu', '')
    return render(request, "index.html", {'menu':menu})

def about(request):
    menu = request.GET.get('menu', '')
    return render(request, "about.html", {'menu':menu})

def works(request):
    menu = request.GET.get('menu', '')
    return render(request, "works.html", {'menu':menu})

def blog(request, tag_slug=None):
    menu = request.GET.get('menu', '')
    posts = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    return render(request,'blog.html', {'posts': posts,'tag': tag,'menu':menu})

def blog_detail(request, year, month, day, post):
    menu = request.GET.get('menu', '')
    post = get_object_or_404(Post, 
                             slug=post,
                             status='published', 
                             publish__year=year, 
                             publish__month=month, 
                             publish__day=day)
    return render(request,'blog_detail.html', {'post': post, 'menu':menu})


def contact(request):
    menu = request.GET.get('menu', '')
    return render(request, "contact.html", {'menu':menu})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message. We will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


logger = logging.getLogger(__name__)
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                if Subscription.objects.filter(email=email).exists():
                    logger.info(f"Subscription attempt with existing email: {email}")
                    return render(request, 'exists.html')  # Email already exists
                else:
                    Subscription.objects.create(email=email)
                    logger.info(f"New subscription created for email: {email}")
                    return render(request, 'thank_you.html')  # New subscription created
            except Exception as e:
                logger.error(f"Error while processing subscription for email {email}: {e}")
                return render(request, 'error.html')  # Render an error page if needed
    else:
        form = SubscriptionForm()
    
    return redirect(request.META.get('HTTP_REFERER', '/home?menu=home'))


