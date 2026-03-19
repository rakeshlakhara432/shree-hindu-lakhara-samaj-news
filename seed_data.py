import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.news.models import Category, News, Notice
from apps.events.models import Event
from apps.gallery.models import Album, Photo

categories = [
    ('समाज समाचार', 'society-news'),
    ('राजस्थान', 'rajasthan'),
    ('भारत', 'india'),
    ('शिक्षा', 'education'),
    ('धर्म', 'religion'),
    ('व्यापार', 'business'),
    ('तकनीक', 'technology'),
    ('सामाजिक', 'social'),
    ('सरकारी योजनाएं', 'govt-schemes')
]

for cat_name, cat_slug in categories:
    cat, _ = Category.objects.get_or_create(name=cat_name)
    cat.slug = cat_slug
    cat.save()
    
    # Ensure there's at least one news for each category
    news_title = f'{cat_name} के क्षेत्र में बड़ी उपलब्धि'
    news, created = News.objects.get_or_create(
        title=news_title,
        category=cat,
        defaults={
            'content': f'यह {cat_name} से जुड़ी एक महत्वपूर्ण खबर है। समाज के विकास के लिए यह एक बड़ा कदम है। अधिक जानकारी के लिए बने रहें।',
            'tags': f'{cat_name}, SHLS, News',
            'slug': slugify(news_title) if slugify(news_title) else f"{cat_slug}-update"
        }
    )
    if not news.slug:
        news.slug = f"{cat_slug}-news-{news.id}"
        news.save()

# Add sample notices
Notice.objects.get_or_create(
    title='मासिक बैठक — 22 मार्च, जोधपुर समाज भवन',
    defaults={
        'content': 'सभी समाज बंधुओं को सूचित किया जाता है कि आगामी मासिक बैठक 22 मार्च को जोधपुर समाज भवन में आयोजित की जाएगी। आपकी उपस्थिति अनिवार्य है।',
        'is_active': True
    }
)

# Add sample events
from django.utils import timezone
Event.objects.get_or_create(
    title='Mega Health Camp',
    defaults={
        'description': 'Free health checkup camp for all community members.',
        'date': timezone.now() + timezone.timedelta(days=30),
        'venue': 'Jodhpur City Hall',
        'fees': 0
    }
)

# Add sample album
Album.objects.get_or_create(title='वार्षिक महोत्सव 2025', defaults={'description': 'समाज के वार्षिक महोत्सव की झलकियां'})

print("Seeding complete.")
