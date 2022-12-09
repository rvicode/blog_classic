from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.decorators.http import require_GET

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
    paginate_by = 1


@require_GET
def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    category = Category.objects.all()[:10]
    articles = Article.objects.all().order_by('-datetime_create')[:3]
    if request.method == 'POST':
        massage = request.POST.get('message')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(article=article, username=request.user, massage=massage, parent_id=parent_id)
    return render(request, 'pages/detail_post.html',
                  {'article': article, 'articles': articles, 'category': category})
