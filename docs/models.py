from django.db import models
from django.contrib.auth.models import User

class OrgMst(models.Model):
    org_id = models.AutoField(primary_key=True)
    org_name = models.CharField(max_length=100)
    org_type = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    admin = models.IntegerField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)


class ProjectMst(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    project_base_url = models.CharField(max_length=50)
    project_base_port = models.IntegerField(default=8000, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)


class Api(models.Model):
    method_choices = [
        ('POST', 'POST'),
        ('GET', 'GET'),
        ('PUT', 'PUT'),
        ('PATCH', 'PATCH'),
        ('DELETE', 'DELETE')
    ]
    api_id=models.AutoField(primary_key=True)
    project = models.ForeignKey(ProjectMst, models.DO_NOTHING)
    api_name = models.CharField(max_length=50)
    api_endpoint = models.CharField(max_length=100)
    api_sample_url = models.CharField(max_length=100)
    api_port = models.IntegerField()
    api_method = models.CharField(max_length=10, choices=method_choices)
    api_description = models.TextField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)


class ApiParams(models.Model):
    param_id=models.AutoField(primary_key=True)
    api = models.ForeignKey(Api, models.DO_NOTHING)
    param_name = models.CharField(max_length=100)
    param_type = models.CharField(max_length=100)
    param_required = models.BooleanField()
    param_sample = models.CharField(max_length=100)


class ApiSamples(models.Model):
    sample_id=models.AutoField(primary_key=True)
    api = models.ForeignKey(Api, models.DO_NOTHING)
    input = models.TextField()
    output = models.TextField()
    status = models.IntegerField()

class TestTable(models.Model):
    name = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)




