from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()

class Use(models.Model):
    uses = models.CharField(max_length=50)

    def __str__(self):
        return self.uses

class DonorProfile(models.Model):
    bio = models.TextField()

    def __str__(self):
        if hasattr(self, 'donor'):
            return f"Profile for {self.donor}"
        else:
            return "Unassigned Profile"
    
    class Meta:
        verbose_name_plural = "Donor Profiles"

class Donor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile = models.OneToOneField(DonorProfile, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Seed(models.Model):
    class SeedType(models.TextChoices):
        HYBRID = "Hybrid", _("Hybrid")
        OPEN_POLLINATED = "Open-Pollinated", _("Open-Pollinated")
        HEIRLOOM = "Heirloom", _("Heirloom")

    name = models.CharField(max_length=100)
    botanical = models.CharField(max_length=150)
    seed_type = models.CharField(max_length=15, choices=SeedType.choices, default=SeedType.HYBRID)
    continent = models.CharField(max_length=20)
    use = models.ForeignKey(Use, on_delete=models.SET_NULL, null=True, related_name="seeds")
    donors = models.ManyToManyField(Donor, related_name="seeds")
    slug = models.SlugField(max_length=500, null=True, db_index=True, help_text="SEO-friendly URLs")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("seeds-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)