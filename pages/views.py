from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Article, Category, Comment


class HomeView(generic.ListView):
    http_method_names = ['get']
    queryset = Article.objects.all()[:6]
    template_name = 'pages/home.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()[:6]
        return context


class AllArticleView(generic.ListView):
    http_method_names = ['get']
    model = Article
    template_name = 'pages/all_post.html'
    context_object_name = 'article'
    paginate_by = 6


def article_category_view(request, pk):
    category = get_object_or_404(Category, id=pk)
    article = Article.objects.filter(category=category)
    paginator = Paginator(article, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/all_post.html', {'article': page_obj})


def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    category = Category.objects.all()[:10]
    articles = Article.objects.all().order_by('-datetime_create')[:3]

    if request.method == 'POST':
        massage = request.POST.get('message')
        parent_id = request.POST.get('parent_id')

        Comment.objects.create(article=article, username=request.user, massage=massage, parent_id=parent_id)
        messages.success(request, 'Your comment was successfully ! ')
    return render(request, 'pages/detail_post.html',
                  {'article': article, 'articles': articles, 'category': category})
