from django.urls import path
from . import views

app_name = 'blog'  # Define the namespace for this app

urlpatterns = [
# I don't use this urls.py
    path('blog/', views.blog, name='blog'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.blog_detail, name='blog_detail'),
]