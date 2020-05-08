from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .yasg import urlpatterns as doc_urls
from . import views


router = DefaultRouter()
router.register('polls', views.PollViewSet)
router.register('questions', views.QuestionViewSet)
# router.register('users', views.UserViewSet)


urlpatterns = [
    path('users/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve'}))
]

urlpatterns += router.urls
# urlpatterns += doc_urls
