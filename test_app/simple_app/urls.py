from django.urls import path

from . import views


app_name = 'simple_app'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('api', views.Api.as_view(), name='api'),
]
