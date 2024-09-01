from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news' : news,
        "categories" : categories
    }

    return render(request, 'news/home.html', context)



def contactPageView(request):
    print(request.POST)
    form = ContactForm(request.POST or None)
    if request.method == "POST" and  form.is_valid():
        form.save()
        return HttpResponse("<h2> Biz bilan bo'glanganingiz uchun tashakkur!")
    context = {
        "form": form
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