from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Jobs(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    job_heading=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    location=models.CharField(max_length=100)
    start_date=models.DateField()
    salary=models.IntegerField(default=10000)
    apply_by=models.DateField()
    job_type=models.CharField(max_length=255)
    available=models.IntegerField()
    about_company=models.TextField()
    about_job=models.TextField()
    skills=models.TextField()
    requirements=models.TextField()
    why_us=models.TextField()
    def __str__(self):
        return self.job_heading
    class Meta:
        verbose_name='Job posted by Employer'