from django.urls import include, path
from rest_framework.routers import DefaultRouter

from posts.models import Follow, Comment
from api.views import (CommentViewSet, FollowViewSet, GroupViewSet,
                       PostViewSet, UserViewSet)

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register('posts/(?P<post_id>\\d+)/comments',
                CommentViewSet,
                basename=Comment)
router.register(r'users', UserViewSet)
router.register(r'follow', FollowViewSet, basename=Follow)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
