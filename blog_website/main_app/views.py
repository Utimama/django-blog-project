from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def home_page_view(request):
    all_article=Post.objects.all()
    context={
        "articles":all_article,
        
    }
    return render(request,"main/index.html", context)

def about_page_view(request):
    return render(request, "main/about.html")

def contact_page_view(request):
    return render(request, "main/contact.html")


def single_blog_post(request, blog_id):
    post=Post.objects.get(id=blog_id)
    categories=Category.objects.all()
    similar_post=Post.objects.filter(category=post.categories).exclude(id=post.id)
    context={
        "article":post,
        "categories":categories,
        "similar_articles":similar_post
    }
    return render(request, "main/post.html", context)


