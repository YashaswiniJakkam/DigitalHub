from django.db import models
from django.utils.text import slugify
from authentication.models import Student,Mentor


class ProblemStatements(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Title')
    prerequisites = models.TextField(verbose_name='List of Prerequisites')
    description = models.TextField(verbose_name='Description')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[
        ('ongoing', 'Ongoing'),
        ('finished', 'Finished'),
        ('not started', 'Not Started'),
    ],default='not started', verbose_name='Status')
    students_working_on = models.ManyToManyField(Student, blank=True,related_name='problems')
    mentors_assigned = models.ManyToManyField(Mentor, blank=True, related_name='assigned_problem_statements')
    mentors_applied = models.ManyToManyField('MentorApplication', blank=True, related_name='applied_problem_statements')
    livelink = models.CharField(verbose_name='live link', blank=True, max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class MentorApplication(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    problem_statement = models.ForeignKey(ProblemStatements, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    class Meta:
        unique_together = ['mentor', 'problem_statement']

