from django.urls import path
# The . works since we are in same folder i.e. blog
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    # When someone comes to this urls.py file, is there any path that is an int? (could also be string, slug, etc.)
    path('<int:blog_id>/', views.detail, name = 'detail'),
]
