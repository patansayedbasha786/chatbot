
from django.urls import path
from . import views

urlpatterns = [
    path("", views.chatbot_page, name="chatbot"),
    path("api/search/", views.search_images, name="search_images"),
]
