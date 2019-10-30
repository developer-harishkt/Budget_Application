"""budgetproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from . import views
from budget.apis import views as api_views

urlpatterns = [
    path('email', views.sendEmail, name='sendEmail'),
    path('', views.project_list, name='list'),
    path('add', views.ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>', views.project_detail, name='detail'),

    # REST API Urls

    path('api/project', api_views.ProjectCreateView.as_view()),
    path('api/project/<int:pk>', api_views.ProjectDetailView.as_view()),
    path('api/category', api_views.CategoryCreateView.as_view()),
    path('api/category/<int:pk>', api_views.CategoryDetailView.as_view()),
    path('api/expense', api_views.ExpenseCreateView.as_view()),
    path('api/expense/<int:pk>', api_views.ExpenseDetailView.as_view()),
]
