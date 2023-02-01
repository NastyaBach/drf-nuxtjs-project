from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, TagDetailView, TagView, AsideView, RegisterView, ProfileView, AddCommentView, GetCommentView, CommentDeleteView

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path("", include(router.urls)),
    path("tags/", TagView.as_view()),
    path("tags/<slug:tag_slug>/", TagDetailView.as_view()),
    path("aside/", AsideView.as_view()),
    path("register/", RegisterView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("comments/", AddCommentView.as_view()),
    path("comments/<slug:post_slug>/", GetCommentView.as_view()),
    path("comments/delete/<int:comment_id>", CommentDeleteView.as_view()),
]