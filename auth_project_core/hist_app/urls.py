from django.urls import path
from .views import HistListView, HistDetailView, HistCreateView, HistUpdateView

app_name = 'hist_app'

urlpatterns = [
    # Patterns using views 
    path("allhist/", HistListView.as_view(), name="list_view"),
    path("allhist/<int:pk>", HistDetailView.as_view(), name="detail_view"),
    path("allhist/add_hist/", HistCreateView.as_view(), name="create_view"),
    path("allhist/edit_hist/<int:pk>", HistUpdateView.as_view(), name="update_view")
]
