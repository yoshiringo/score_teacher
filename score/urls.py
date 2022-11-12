from django.urls import path
from . import views

app_name = 'score'

urlpatterns = [
    path('', views.PersonList.as_view(),name='person_list'),
    path('detail/<int:pk>/', views.PlayerDetail.as_view(), name='detail'), 
    path('stat_create/<int:pk>/', views.StatCreate.as_view(), name='stat_create'),
]