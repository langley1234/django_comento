from django.urls import path
from . import views

urlpatterns = [
    path("<id>/", views.index, name="index"),
]
