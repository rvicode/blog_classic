from django.shortcuts import render
from django.views import generic

from .models import Article, Category


class HomeView(generic.ListView):
    model = Article
    template_name = 'pages/home.html'
    context_object_name = 'article'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()[:6]
        return context
