from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
	jobs = Job.objects.all()

	jobs_with_ruby = Job.objects.filter(languages_used__language_name__startswith="Ruby")

	context = {'jobs':jobs, 'ruby_jobs':jobs_with_ruby}

	return render(request, "portfolio/index.html", context)

def job_detail(request, job_id):
	job = Job.objects.get(id=job_id)

	return render(request, "portfolio/job_details.html", {"job": job})
