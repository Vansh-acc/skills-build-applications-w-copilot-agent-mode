"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
import os

CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
def get_base_url(request):
    if CODESPACE_NAME:
        return f"https://{CODESPACE_NAME}-8000.app.github.dev"
    return request.build_absolute_uri('/')[:-1]

@api_view(['GET'])
def api_root(request, format=None):
    base_url = get_base_url(request)
    return Response({
        'users': f"{base_url}/api/users/",
        'teams': f"{base_url}/api/teams/",
        'activities': f"{base_url}/api/activities/",
        'workouts': f"{base_url}/api/workouts/",
        'leaderboard': f"{base_url}/api/leaderboard/",
    })

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
