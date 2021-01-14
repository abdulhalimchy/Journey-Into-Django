from django.urls import path

from . import views

app_name='polls'

urlpatterns = [
    #/polls/
    path('', views.index, name='index'),

    #/polls/4
    path('<int:question_id>/', views.detail, name='detail'),

    #/polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),

    #polls/2/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]