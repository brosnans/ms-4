from django.conf.urls import url
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url(r'^$', PasswordResetView,
        {'post_reset_redirect': reverse('PasswordResetDoneView')}, name='PasswordResetView'),
    url(r'^done/$', PasswordResetDoneView, name='PasswordResetDoneView'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView,
        {'post_reset_redirect': reverse('PasswordResetCompleteView')}, name='PasswordResetConfirmView'),
    url(r'^complete/$', PasswordResetCompleteView, name='PasswordResetCompleteView'),
]
