from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include, reverse_lazy
from accounts.views import register

app_name = 'accounts'

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register/', register, name='register'),
    path('change_password/',
         PasswordChangeView.as_view(
             template_name="registration/password_change_form.html",
             success_url=reverse_lazy("accounts:password_change_done")
         ),
         name='password_change'),

    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'
        ),
        name='password_change_done')

]