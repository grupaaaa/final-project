from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include, reverse_lazy
# from accounts.views import register
from accounts.views import UserRegisterView

# app_name = 'accounts'

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('register/', UserRegisterView.as_view(success_url=reverse_lazy('login')), name='register'),
    path('change_password/',
        PasswordChangeView.as_view(
            template_name="registration/password_change_form.html",
            success_url=reverse_lazy('password_change_done')
        ),
        name='password_change'),

    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'),
        name='password_change_done'),

    path('password_reset/',
        PasswordResetView.as_view(
            success_url=reverse_lazy("password_reset_done"),
            template_name='registration/password_reset_form.html',
            email_template_name='registration/password_reset_email.html',
        ),
        name='password_reset'),

    path('password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html',
            success_url=reverse_lazy("password_reset_done")
        ),
        name='password_reset_confirm'),

    path('reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html',
        ),
        name='password_reset_complete')
]