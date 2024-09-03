from idlelib.help_about import AboutDialog
from tkinter.font import names

from django.urls import path
from .views import news_list, news_detail, Page404View, aboutPageView, ContactPageView, HomePageView #contactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home_page'),
    path('news/', news_list, name = "all_news_list"),
    path('news/<int:id>/', news_detail, name = "news_detail_page"),
    path('contact-us/', ContactPageView.as_view(), name = 'contact_page'),
    path('404/', Page404View, name = '404_page'),
    path('about/', aboutPageView, name = 'about_page' )
]