from django.db import models
from django.utils.text import slugify

class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    registration_limit = models.PositiveIntegerField(default=0, help_text="0 for unlimited")
    fees = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='events/')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
