from django.urls import path
from .views import RecommendResourcesView

urlpatterns = [
    path('recommend/', RecommendResourcesView.as_view(), name='recommend-resources'),
]
