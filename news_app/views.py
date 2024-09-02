from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import News, Category
from .forms import ContactForm

def news_list(request):
    news_list = News.published.all() # 1 chi usul
    # news_list = News.objects.filter(status=News.Status.Published) # 2 chi usul
    context = {
        "news_list":news_list
    }
    return render(request, "news/news_list.html", context)

def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        "news":news
    }

    return render(request, 'news/news_detailed.html', context)

def homePageView(request):
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:10]
    local_one = News.published.filter(category__name="Mahalliy").order_by("-publish_time")[:1]
    local_news = News.published.all().filter(category__name="Mahalliy").order_by("-publish_time")[1:6]

    context = {
        'news_list' : news_list,
        "categories" : categories,
        "local_one" : local_one,
        "local_news" : local_news,
    }

    return render(request, 'news/home.html', context)



# def contactPageView(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and  form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Biz bilan bo'glanganingiz uchun tashakkur!</h2>")
#     context = {
#         "form": form
#     }
#
#     return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form' : form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bo'glanganingiz uchun tashakkur!</h2>")
        context = {
            "form" : form
        }
        return render(request, 'news/contact.html', context)

def Page404View(request):
    context = {

    }
    return render(request, 'news/404.html', context)

def aboutPageView(request):
    context = {

    }

    return render(request, 'news/about.html', context)