from django.shortcuts import render
from django.views import generic

from .models import Chapter, Member

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'members/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Returns the members personal information to be displayed on the index profile page
        """
        return Member.objects

class DetailView(generic.DetailView):
    model = Member
    template_name = 'members/detail.html'
