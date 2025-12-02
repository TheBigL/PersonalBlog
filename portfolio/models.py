from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=100, verbose_name="Portfolio Name")
    description = models.TextField(verbose_name="Portfolio Description")
    img = models.ImageField(upload_to='portfolio_images/', verbose_name="Portfolio Image")
    link = models.URLField(max_length=200, verbose_name="Portfolio Link")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
        ordering = ['-created_at']