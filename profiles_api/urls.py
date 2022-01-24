from django.urls import path
from . import views

urlpatterns = [
    path('hello-view/',views.HelloAppiView.as_view()),
]
