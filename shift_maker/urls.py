from django.urls import path
from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path("choice_page/", views.choice_page, name="choice_page"),
    path("default/", views.default, name="default"),
    path("irregular/", views.irregular, name="irregular"),
]