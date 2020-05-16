from django.urls import path
from .views import (
    ProjectListView,
    ProjectAddView
)

app_name = 'portfolioapi'

urlpatterns = [
    path('list', ProjectListView.as_view(), name='list'),
    path('add', ProjectAddView.as_view(), name='new')
]