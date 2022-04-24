"""project_741 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import include, path
from rest_framework import routers
from api.views import viewtest
from api.views import commentview
from api.views import postview
from api.views import user_profileview
from api.views import comment_replayview

router = routers.DefaultRouter()
router.register(r'users', viewtest.UserViewSet)
router.register(r'groups', viewtest.GroupViewSet)
router.register(r'user', user_profileview.ProfileViewSet)
router.register(r'posts', postview.PostViewSet)
router.register(r'comment', commentview.CommentViewSet)
router.register(r'comment_replay', comment_replayview.CommentReplayViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('__debug__/', include('debug_toolbar.urls')),
]

