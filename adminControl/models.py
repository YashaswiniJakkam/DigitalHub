from django.db import models

# Create your models here.
class ProblemStatements(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    mentor_name = models.CharField(max_length=100, verbose_name='Mentor Name')
    contact_mail = models.EmailField(verbose_name='Contact Email')
    mentor_pic = models.ImageField(upload_to='mentor_pics/', null=True, blank=True, verbose_name='Mentor Picture')
    prerequisites = models.TextField(verbose_name='List of Prerequisites')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title