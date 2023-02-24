
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from django.views.generic import ListView, View
from newsapi import NewsApiClient

from .models import NewsItem

import environ

env = environ.Env()
environ.Env.read_env()
API_KEY = env("API_KEY")

class NewsItemListView(ListView):
    model = NewsItem
    template_name = 'news_item_list.html'
    context_object_name = 'news_items'
    ordering = ['-published_at']
    paginate_by = 20

class NewsItemAPIView(View):
    def get(self, request):
        newsapi = NewsApiClient(api_key=API_KEY)
        all_articles = newsapi.get_everything(domains='bbc.co.uk,techcrunch.com', language='en')
        if all_articles["status"] == "ok":
            news_items = all_articles['articles']
            for item in news_items:
                # parse response and save in database
                NewsItem.objects.create(
                    source=item['source']['id'],
                    author=item['author'],
                    title=item['title'],
                    description=item['description'],
                    url=item['url'],
                    image_url=item['urlToImage'],
                    published_at=parse_datetime(item['publishedAt']),
                    content=item['content']
                )
            # return 100 most recent news items in JSON format from database
            news_items = NewsItem.objects.order_by('-published_at')[:100]
            data = [{
                    'source': item.source, 
                    'author': item.author, 
                    'title': item.title, 
                    'description': item.description, 
                    'url': item.url, 
                    'image_url': item.image_url, 
                    'published_at': item.published_at.isoformat(), 
                    'content': item.content
                    } for item in news_items]
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'error': 'Unable to fetch news items.'})

class Handle404View(View):
    def get(self, request, exception=None, *args, **kwargs):
        return render(request, '404.html', status=404)