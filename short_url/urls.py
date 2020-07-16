from django.contrib import admin
from django.urls import path
from short_url.views import ShortUrlView,UrlRedirectView
# from users.views import SearchView
urlpatterns = [
    path('',ShortUrlView.as_view(),name='home-page'),
    path('<slug:shortcode>',UrlRedirectView.as_view(),name='redirect'),
    # path('search/', SearchView.as_view(), name='search'),

]
































