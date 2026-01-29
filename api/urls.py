from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    ProfileView,
    ProfileSearchView,
    PublicProfileView
)

urlpatterns = [
    path("auth/register/", RegisterView.as_view()),
    path("auth/login/", LoginView.as_view()),

    path("profile/", ProfileView.as_view()),
    path("profiles/search/", ProfileSearchView.as_view()),
    path("profile/public/<str:username>/", PublicProfileView.as_view()),
]
