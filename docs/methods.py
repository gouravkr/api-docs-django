from docs.models import Api, ApiParams, ProjectMst, ApiSamples
from django.forms import ModelForm

def create_project(**kwargs):
    pass

class EditAPI:
    """Class for adding, editing, and deleting APIs"""

    def create(body):
        api_fields = ["api_name", "api_endpoint", "api_sample_url", "api_port", "api_method",
                      "api_description", "project"]
        samples_fields = ['input', 'output', 'status']
        api_input = {key: body[key] for key in api_fields}
        sample_input = {key: body[key] for key in samples_fields}

        create_api = ApiForm(api_input)
        api = create_api.save()
        sample_input.update({'api': api.pk})

        create_sample = SamplesForm(sample_input)
        sample = create_sample.save()
        response = {"api": api.pk, "sample": sample.pk}
        return response

    def fetch(project_id, id=None):
        if id is not None:
            records = Api.objects.filter(project=project_id, pk=id)
            records = list(records.values())
        else:
            records = Api.objects.filter(project=project_id)
            records = list(records.values())
        return records

    
class ApiForm(ModelForm):
    class Meta:
        model = Api
        fields = ['api_name', 'api_endpoint', 'api_sample_url', 'api_port', 'api_method', 'api_description', 'project']

class SamplesForm(ModelForm):
    class Meta:
        model = ApiSamples
        fields = ['api','input','output','status']
        
class ProjectForm(ModelForm):
    class Meta:
        model = ProjectMst
        fields = ['project_name', 'project_description',
                  'project_base_url', 'project_base_port', 'created_by']


class Projects:
    """methods to fetch and create projects"""

    def __init__(self, project_id=None):
        if project_id is not None:
            self.project_id = project_id

    def create_project(self, body):
        body['created_by'] = 1
        create_project = ProjectForm(body)
        response = create_project.save()
        return response

    def fetch_project(self, search_string=None):
        if hasattr(self, 'project_id'):
            projects = ProjectMst.objects.filter(pk=self.project_id)
            projects = projects.values()
        elif search_string is not None:
            projects = ProjectMst.objects.filter(project_name__contains=search_string)
            projects = projects.values()
        else:
            projects = ProjectMst.objects.values()
        return list(projects)

    def modify_project(self, body):
        pass
