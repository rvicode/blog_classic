from django.shortcuts import render
from django.views import  generic

from .models import Article


class HomeView(generic.ListView):
    model = Article
    template_name = 'pages/home.html'
    context_object_name = 'article'
    paginate_by = 6
