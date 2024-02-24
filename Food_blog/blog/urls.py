from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profile/', include([
        path('create/', ProfileCreateView.as_view(), name='profile-create'),
        path('details/', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
        path('dashboard/', GameDashboardView.as_view(), name='game-dashboard'),
    ])),

    path('game/', include([
        path('create/', BlogCreateView.as_view(), name='game-create'),
        path('details/<int:pk>/', BlogDetailsView.as_view(), name='game-details'),
        path('edit/<int:pk>/', BlogEditView.as_view(), name='game-edit'),
        path('delete/<int:pk>/', blog_delete, name='game-delete'),
    ]))
]