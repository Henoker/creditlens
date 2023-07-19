from django.urls import path
from.  import views

urlpatterns = [
    path('', views.homepage, name="index"),
    path('dashboard/', views.dashboard, name="dashboard"),
]