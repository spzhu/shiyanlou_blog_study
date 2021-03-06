from django.shortcuts import render
from django.http import HttpResponse, Http404
from article.models import Article
from datetime import datetime

# Create your views here.
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})
