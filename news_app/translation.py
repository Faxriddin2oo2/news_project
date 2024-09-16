from modeltranslation.translator import register, TranslationOptions

from .models import News, Category


@register(News) # 1-usul
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

# translator.register(News, NewsTranslationOptions) # 2-usul

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)