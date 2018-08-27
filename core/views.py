from django.views.generic import TemplateView

# Create your views here.
from core.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all().filter(
            is_published=True
        ).order_by("published_at")[:10]
        return context
