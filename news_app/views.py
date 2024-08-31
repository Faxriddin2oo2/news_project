from lib2to3.fixes.fix_input import context
from msilib.schema import ListView

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import News, Category

def news_list(request):
    news_list = News.published.all() # 1 chi usul
    # news_list = News.objects.filter(status=News.Status.Published) # 2 chi usul
    context = {
        "news_list":news_list
    }
    return render(request, "news/news_list.html", context)
# class NewsListView(ListView):
#     model = News
#     template_name = 'news/news_list.html'
#     context_object_name = 'news_list'

def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        "news":news
    }

    return render(request, 'news/news_detailed.html', context)
# class NewsDetailView(DetailView):
#     model = News
#     template_name = "news/news_detailed.html"