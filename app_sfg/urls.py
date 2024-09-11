from django.urls import path
form . import views

urlpatterns = [
    path("", views.IndexPage, name="index")
]
