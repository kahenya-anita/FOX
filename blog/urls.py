from django.urls import path
from blog.views import ListCreatePostAPIView, RetrieveUpdateDestroyPostAPIView

urlpatterns = [
    path("posts", ListCreatePostAPIView.as_view(), name="create_list_posts"),
    path(
        "posts/<str:pk>",
        RetrieveUpdateDestroyPostAPIView.as_view(),
        name="retrieve_update",
    ),
]
