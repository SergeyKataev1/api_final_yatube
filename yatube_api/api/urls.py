from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

routerV1 = DefaultRouter()
routerV1.register("posts", PostViewSet, basename="posts")
routerV1.register("groups", GroupViewSet, basename="groups")
routerV1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)
routerV1.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(routerV1.urls)),
    path("v1/", include("djoser.urls.jwt")),
]
