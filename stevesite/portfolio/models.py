from django.db import models

# Create your models here.
class Job(models.Model):
	company_name = models.CharField(max_length=256)
	job_title = models.CharField(max_length=256)
	start_date = models.DateField()
	end_date = models.DateField()
