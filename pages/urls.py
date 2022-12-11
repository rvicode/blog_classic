from django.urls import path

from . import views


app_name = 'pages'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('detail/<int:pk>', views.article_detail, name='detail_post'),
    path('all', views.AllArticleView.as_view(), name='all_post'),
    path('all/<int:pk>', views.article_category, name='all_post_with_category'),
]
