from django.urls import path
from .views import NewsItemListView, NewsItemAPIView, Handle404View

urlpatterns = [
    path('', NewsItemListView.as_view(), name='news_item_list'),
    path('api/', NewsItemAPIView.as_view(), name='news_item_api'),
    path('<path:unknown>/', Handle404View.as_view(), name='news_item_error'),
]
