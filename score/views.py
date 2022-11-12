from django.views import generic
from .models import Person, Stat
from .forms import StatCreateForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, get_list_or_404
from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.
class PersonList(generic.ListView):
    model = Person
    template_name = "score/index.html"
    paginate_by = 2


class StatCreate(generic.CreateView):
    model = Stat
    fields = ("date", "total_score", "ob", "penalty", "fw", "par_on", "putt")
    template_name = "score/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get("pk")
        person = get_object_or_404(Person, pk=pk)
        context["person"] = person
        stats = list(Stat.objects.filter(player=pk))
        context["stats"] = person
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.player_id = self.kwargs.get("pk")
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse_lazy("score:detail", kwargs={"pk": pk})
