"""api_docs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from docs import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.API.as_view(), name='create_api'),
    path('projects/<int:id>/', views.Project.as_view(), name='projects'),
    path('projects/<int:project_id>/apis', views.API.as_view(), name='APIs'),
    path('projects/', views.Project.as_view(), name='projects'),
    path('sample/', views.samples, name='sample'),
    path('auth/', obtain_jwt_token, name='auth'),
]
