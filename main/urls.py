from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('devis', views.devis, name='devis'),
    path('contact/', views.contact, name='contact'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:article_id>/', views.article_detail, name='article-detail'),
    path('ajouter_avis/', views.traiter_avis, name='traiter_avis'),
]


