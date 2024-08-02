from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views #new
from home.views import subscribe
from home.views import contact_view

from home import views

urlpatterns = [
    path('admin/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'), #new    
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('works', views.works, name="works"),    
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"), 
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls', namespace='home')),
    path('subscribe/', subscribe, name='subscribe'),
    path('contact/', contact_view, name='contact'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)