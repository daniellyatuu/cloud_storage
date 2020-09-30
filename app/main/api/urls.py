from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.CreatePostView.as_view(), name='create_post'),
]
