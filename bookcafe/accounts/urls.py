from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
urlpatterns=[
    path("login/", LoginView.as_view(template_name="accounts/login.html",next_page="/app/")),
    path("logout/",LogoutView.as_view(next_page="/app/"))
]