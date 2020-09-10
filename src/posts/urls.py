from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'api'

router = routers.SimpleRouter()
router.register(r'posts', views.PostViewSet, basename='post')


urlpatterns = [
    path('', include(router.urls)),

]
