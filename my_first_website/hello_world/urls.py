from django.urls import path
from hello_world import views

# Creates list of URL patterns corresponding to various view functions
urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]