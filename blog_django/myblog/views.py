from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def index(request):
    queryset = Post.objects.all()
    # paginator = Paginator(queryset, 2)
    context ={
        'queryset': queryset
    }
    return render(request,'index.html', context)

def blog(request, blog_id):
    blog = get_object_or_404(Post, id=blog_id)
    context ={
        'blog': blog
    }
    return render(request,'blog.html', context)
