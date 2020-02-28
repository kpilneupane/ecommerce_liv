import view as view
from django.shortcuts import render,redirect,get_object_or_404
from home.models import Items

# Create your views here.

class BaseView(view):
    template_context = {
        'items' : Items.objects.all()
    }
class HomeView(BaseView):
    def __get__(self, request):
        self.template_context['items'] = Items.objects.all()

        return render(request, 'shop-index.html', self.template_context)