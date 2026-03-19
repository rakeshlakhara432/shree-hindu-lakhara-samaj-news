from django.urls import path
from .views import HomeView, NewsByCategoryView, NewsDetailView, EventListView, GalleryListView, NoticeListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug:slug>/', NewsByCategoryView.as_view(), name='news_category'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('gallery/', GalleryListView.as_view(), name='gallery_list'),
    path('notices/', NoticeListView.as_view(), name='notice_list'),
]
