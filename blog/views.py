# get object_or_404 tries to get object or sends back a does not exist error
from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    # Ordering by negative data makes most recent come first
    # The :5 forces only first five to show
    blogs = Blog.objects.order_by('-date')[:5];
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    # Try to grab object for the id or return a 404; pk refers to primary key
    blog = get_object_or_404(Blog, pk=blog_id)
    # In dict, pass forward key as 'id' and its corresponding value is blog_id
    return render(request, 'blog/detail.html', {'blog':blog})
