from django.shortcuts import render

from blog.models import Post


# Create your views here.

def liste_articles(request):
    articles = Post.objects.all()
    return render(request, 'blog/liste_article.html', {'articles': articles})
