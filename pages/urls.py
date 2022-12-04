from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail_post'),
]
