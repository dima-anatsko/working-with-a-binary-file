from django.urls import path
from .views import FileView


app_name = "api"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('keys/', FileView.as_view()),
    path('keys/<slug:key>', FileView.as_view())
]
