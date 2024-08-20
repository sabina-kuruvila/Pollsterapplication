from django.urls import path

from . import views


urlpatterns =[
    path('',views.index,name="index"),
    path('polls/',views.polls,name="polls"),
    path('choices/<int:question_id>/',views.choices,name="choices"),
    path('results/<int:question_id>/',views.results,name="results"),
    path('votes/<int:question_id>/',views.votes,name="votes"),
]
