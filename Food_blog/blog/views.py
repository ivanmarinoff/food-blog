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

from .. import blog


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
    success_url = reverse_lazy('dashboard')


class ProfileDetailsView(views.View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.first()
        blog_count = Blog.objects.all().count()
        rating_list = [blog.utility for blog in Blog.objects.all()]
        average_rating = sum(rating_list) / len(rating_list) if rating_list else 0.0
        average_rating = f'{average_rating:.1f}'
        context = {
            'profile': profile,
            'blog_count': blog_count,
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


class DashboardView(views.TemplateView):
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['blog'] = Blog.objects.all()
        return context


class BlogCreateView(views.CreateView):
    model = Blog
    form_class = BlogCreateForm
    template_name = 'blog/blog-create.html'
    success_url = reverse_lazy('dashboard')


class BlogDetailsView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = Profile.objects.first()
        blog = Blog.objects.get(pk=pk)
        context = {
            'blog': blog,
            'profile': profile,
        }
        return render(request, 'blog/details-blog.html', context)


class BlogEditView(views.UpdateView):
    model = Blog
    form_class = BlogEditForm
    template_name = 'blog/edit-blog.html'
    success_url = reverse_lazy('dashboard')


def blog_delete(request, pk):
    profile = Profile.objects.first()
    blog = Blog.objects.filter(pk=pk).get()
    form = BlogDeleteForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context = {
        'form': form,
        'profile': profile,
        'blog': blog
    }
    return render(request, 'blog/delete-blog.html', context)