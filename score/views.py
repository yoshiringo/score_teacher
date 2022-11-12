from django.views import generic
from .models import Person, Stat
from .forms import StatCreateForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render




# Create your views here.
class PersonList(generic.ListView):
    model = Person
    template_name = 'score/index.html'
    paginate_by = 2

class PlayerDetail(generic.DetailView):
    model = Person
    template_name = 'score/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['breadcrumbs_list'] = [
            {'name': f'#{pk} {self.object.name}',
             'url': ''}
        ]

        context['stat_create_form'] = StatCreateForm
        return context

class StatCreate(generic.CreateView):
    model = Stat
    form_class = StatCreateForm

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        person = get_object_or_404(Person, pk=pk)

        date = int(self.request.POST.get('date'))
        total_score = int(self.request.POST.get('total_score'))
        ob = int(self.request.POST.get('ob'))
        penalty = int(self.request.POST.get('penalty'))
        fw = int(self.request.POST.get('fw'))
        par_on = int(self.request.POST.get('par_on'))
        putt = int(self.request.POST.get('putt'))

        stat_result = Stat(**form.cleaned_data)
        stat_result.save()

        return redirect('score:detail', pk=pk)
