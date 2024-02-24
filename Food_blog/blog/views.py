from typing import Any
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profile, Blog
from .forms import *
from rest_framework import viewsets
from .serializers import ProfileSerializer, BlogSerializer
from django.views import generic as views


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class IndexView(views.TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context


class ProfileCreateView(views.CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('game-dashboard')


class ProfileDetailsView(views.View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.first()
        games_count = Blog.objects.all().count()
        rating_list = [game.rating for game in Blog.objects.all()]
        average_rating = sum(rating_list) / len(rating_list) if rating_list else 0.0
        average_rating = f'{average_rating:.1f}'
        context = {
            'profile': profile,
            'games_count': games_count,
            'average_rating': average_rating,
        }
        return render(request, 'profile/details-profile.html', context)


class ProfileEditView(views.UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('profile-details')

    def get_object(self, queryset=None):
        # Ensure that the correct profile instance is retrieved based on your logic
        return Profile.objects.first()


class ProfileDeleteView(views.DeleteView):
    model = Profile
    form_class = ProfileDeleteForm
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        # Ensure that the correct profile instance is retrieved based on your logic
        return Profile.objects.first()


class BLogDashboardView(views.TemplateView):
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['games'] = Blog.objects.all()
        return context


class BlogCreateView(views.CreateView):
    model = Blog
    form_class = BlogCreateForm
    template_name = 'game/create-game.html'
    success_url = reverse_lazy('game-dashboard')


class BlopgDetailsView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.first()
        game = Blog.objects.get(pk=pk)
        context = {
            'game': game,
            'profile': profile,
        }
        return render(request, 'game/details-game.html', context)


class BlogEditView(views.UpdateView):
    model = Blog
    form_class = BlogEditForm
    template_name = 'game/edit-game.html'
    success_url = reverse_lazy('game-dashboard')


def blog_delete(request, pk):
    profile = Profile.objects.first()
    game = Blog.objects.filter(pk=pk).get()
    form = BlogDeleteForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect('game-dashboard')
    context = {
        'form': form,
        'profile': profile,
        'game': game
    }
    return render(request, 'game/delete-game.html', context)