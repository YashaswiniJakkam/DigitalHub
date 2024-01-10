from django.db import models
from django.utils.text import slugify

# Create your models here.
class ProblemStatements(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    mentor_name = models.CharField(max_length=100, verbose_name='Mentor Name')
    contact_mail = models.EmailField(verbose_name='Contact Email')
    mentor_pic = models.ImageField(upload_to='media/mentor_pics/', null=True, blank=True, verbose_name='Mentor Picture')
    prerequisites = models.TextField(verbose_name='List of Prerequisites')
    description = models.TextField(verbose_name='Description')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Create a unique slug using the title
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title