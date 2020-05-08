from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('polls', views.PollViewSet)
router.register('polls/(?P<poll_id>[\d]+)/answers', views.SessionsViewSet)
router.register('questions', views.QuestionViewSet)


urlpatterns = [
    path('users/<int:pk>/', views.UserViewSet.as_view({'get': 'retrieve'})),
    path('doc/', include('api.yasg')),
]

urlpatterns += router.urls
