from django.urls import include, path
from rest_framework import routers
from users.views import MeViewSet, SignupViewSet, TokenView, UsersViewSet

from .views import (CategoryViewSet, CommentViewSet, GenresViewSet,
                    ReviewViewSet, TitlesViewSet)

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenresViewSet, basename='genres')
router.register('titles', TitlesViewSet, basename='titles')
router.register('auth/signup', SignupViewSet, basename='signup')
router.register('users', UsersViewSet, basename='users')

router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')

router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/users/me/', MeViewSet.as_view()),
    path('v1/', include(router.urls)),
    path('v1/auth/token/', TokenView.as_view()),
]
