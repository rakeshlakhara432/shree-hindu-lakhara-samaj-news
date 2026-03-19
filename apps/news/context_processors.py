from .models import Category, News, Notice
from apps.events.models import Event

def global_context(request):
    return {
        'all_categories': Category.objects.exclude(name__iexact='Society News'),
        'breaking_news_list': News.objects.filter(is_breaking=True).order_by('-created_at')[:5],
        'recent_notices': Notice.objects.filter(is_active=True).order_by('-created_at')[:3],
        'upcoming_events_sidebar': Event.objects.all().order_by('date')[:3],
    }
