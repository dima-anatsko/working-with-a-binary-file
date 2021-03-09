from django.urls import path

from .views import FileView, LoginApiView, SignUpApiView

app_name = "api"

urlpatterns = [
    path('login', LoginApiView.as_view(), name='login'),
    path('signup', SignUpApiView.as_view(), name='signup'),
    path('keys/', FileView.as_view()),
]
