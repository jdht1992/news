from django.views.generic import ListView
from .models import Article


class NewListView(ListView):
    model = Article
    template_name = 'news-list.html'
    context_object_name = 'articles'

"""
def new_list(request):
    article = Article.objects.all()
    context={
        'article':article
    }
    return render(request, 'news-list.html', context)
"""

