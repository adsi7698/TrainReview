from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'Passengers'

urlpatterns = [
    url(r'^PassengerLogin/$', views.login_view, name="login_view"),
    url(r'^PassengerIntermediate/$', views.intermediate_view, name="intermediate_view"),
    url(r'^PassengerSignup/$', views.signup_view, name="signup_view"),
    url(r'^PassengerLogout/$', views.logout_view, name="logout_view"),
    url(r'^PassengerReview/$', views.review_view, name="review_view"),
    url(r'^PassengerReviewCreated/$', views.review_created, name="review_created"),
    url(r'^PassengerProfile/$', views.profile, name="profile"),
]