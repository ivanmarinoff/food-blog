from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profile/', include([
        path('create/', ProfileCreateView.as_view(), name='profile-create'),
        path('details/', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
        path('dashboard/', DashboardView.as_view(), name='dashboard'),
    ])),

    path('blog/', include([
        path('create/', BlogCreateView.as_view(), name='blog-create'),
        path('details/<int:pk>/', BlogDetailsView.as_view(), name='blog-details'),
        path('edit/<int:pk>/', BlogEditView.as_view(), name='blog-edit'),
        path('delete/<int:pk>/', blog_delete, name='blog-delete'),
    ]))
]