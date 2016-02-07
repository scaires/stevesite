from django.db import models

# Create your models here.


class Language(models.Model):
	language_name = models.CharField(max_length=256)

	def __str__(self):
		return self.language_name


class Job(models.Model):
	company_name = models.CharField(max_length=256)
	job_title = models.CharField(max_length=256)
	start_date = models.DateField()
	end_date = models.DateField()
	languages_used = models.ManyToManyField(Language)

	def __str__(self):
		return self.job_title + ", " + self.company_name