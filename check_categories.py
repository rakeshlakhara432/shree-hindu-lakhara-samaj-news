import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps.news.models import Category

for c in Category.objects.all():
    print(f"Name: {c.name}, Slug: {c.slug}")
