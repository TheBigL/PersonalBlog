from django.db import models
from django.urls import reverse

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=100, verbose_name="Portfolio Name")
    description = models.TextField(verbose_name="Portfolio Description")
    img = models.ImageField(upload_to='portfolio_images/', verbose_name="Portfolio Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    link = models.URLField(max_length=200, blank=True, verbose_name="Portfolio Link")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
        ordering = ['-created_at']

def get_absolute_url(self):
    return reverse("portfolio:portfolio_detail", kwargs={"pk": self.pk})

def snippet(self):
    return self.description[:100] + '...'