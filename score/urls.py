from django.urls import path
from . import views

app_name = "score"

urlpatterns = [
    path("", views.PersonList.as_view(), name="person_list"),
    path("detail/<int:pk>/", views.StatCreate.as_view(), name="detail"),
]
