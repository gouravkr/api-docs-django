from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json

from .methods import EditAPI, ApiForm, SamplesForm, ProjectForm, Projects
from .models import ProjectMst, ApiSamples

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class API(View):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        response = EditAPI.create(body)
        return JsonResponse(response, safe = False)

    def get(self, request, project_id):
        results = EditAPI.fetch(project_id)
        return JsonResponse(results, safe=False)

@csrf_exempt
def samples(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    add_samples = SamplesForm(body)
    sample = add_samples.save()
    return HttpResponse(sample.pk)


@method_decorator(csrf_exempt, name='dispatch')
class Project(View):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        project = Projects()
        response = project.create_project(body)
        return HttpResponse(response)
    
    def get(self, request, id=None):
        search_string = request.GET.get('search', None)
        project = Projects(id)
        response = project.fetch_project(search_string)
        return JsonResponse(response, safe=False)
