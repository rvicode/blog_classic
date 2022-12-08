from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Article, Category, Comment


class HomeView(generic.ListView):
    model = Article
    template_name = 'pages/home.html'
    context_object_name = 'article'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()[:6]
        return context


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
