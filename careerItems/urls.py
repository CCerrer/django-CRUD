from django.urls import path
from .views import ItemListView, ItemDetailView

app_name = 'careerItems'

urlpatterns = [
    path('items/', ItemListView.as_view(), name='items-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='items-detail'),
]
