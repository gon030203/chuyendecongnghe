from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), # Changed from views.index
    path("<int:pk>/", views.DetailView.as_view(), name="detail"), # Changed from views.detail
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"), # Changed from views.results
    path("<int:question_id>/vote/", views.vote, name="vote"),
]