from django.urls import path

from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:pk>', views.article_detail, name='detail_post'),
]
