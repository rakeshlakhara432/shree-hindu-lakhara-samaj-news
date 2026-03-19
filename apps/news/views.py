from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import News, Category, Notice
from apps.events.models import Event
from apps.gallery.models import Album

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_news'] = News.objects.all().order_by('-created_at')[:6]
        context['breaking_news'] = News.objects.filter(is_breaking=True).order_by('-created_at')[:5]
        context['upcoming_events'] = Event.objects.all().order_by('date')[:3]
        context['notices'] = Notice.objects.filter(is_active=True).order_by('-created_at')[:4]
        context['categories'] = Category.objects.all()
        return context

class NewsByCategoryView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return News.objects.filter(category=self.category).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        return context

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_news'] = News.objects.filter(category=self.object.category).exclude(id=self.object.id)[:4]
        return context

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 9

class GalleryListView(ListView):
    model = Album
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'albums'
    paginate_by = 12

class NoticeListView(ListView):
    model = Notice
    template_name = 'news/notice_list.html'
    context_object_name = 'notices'
    paginate_by = 15
    queryset = Notice.objects.filter(is_active=True).order_by('-created_at')
