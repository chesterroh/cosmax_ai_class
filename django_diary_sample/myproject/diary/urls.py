from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('view/<int:diary_id>/', views.viewdiary, name='viewdiary'),
    path('save/', views.save, name='save'),
    path('amend/<int:diary_id>/', views.amend, name='amend'),
    path('delete/<int:diary_id>/', views.delete, name='delete'),
]