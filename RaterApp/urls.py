from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MealViewSet, RatingViewSet, UserViewSet

from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register('meals', viewset=MealViewSet)
router.register('ratings', viewset=RatingViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', ObtainAuthToken.as_view()),

]
