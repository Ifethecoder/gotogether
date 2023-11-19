from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('sign-up', sign_up, name='sign_up'),
    path('create-post', create_post, name='create_post'),
    path('details/<int:id>', details, name='details'),
]