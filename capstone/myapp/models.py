from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Seed(models.Model):
    class SeedType(models.TextChoices):
        HYBRID = "Hybrid", _("Hybrid")
        OPEN_POLLINATED = "Open-Pollinated", _("Open-Pollinated")
        HEIRLOOM = "Heirloom", _("Heirloom")

    name = models.CharField(max_length=100)
    botanical = models.CharField(max_length=150)
    seed_type = models.CharField(max_length=15, choices=SeedType.choices, default=SeedType.HYBRID)
    continent = models.CharField(max_length=20)
    slug = models.SlugField(max_length=500, null=True, db_index=True, help_text="SEO-friendly URLs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("seeds-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)